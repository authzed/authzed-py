import asyncio
import uuid
from typing import Any, Literal

import pytest
from google.protobuf.struct_pb2 import Struct

from authzed.api.v1 import (
    AsyncClient,
    BulkCheckPermissionRequest,
    BulkCheckPermissionRequestItem,
    BulkExportRelationshipsRequest,
    BulkImportRelationshipsRequest,
    CheckPermissionRequest,
    CheckPermissionResponse,
    Client,
    Consistency,
    ContextualizedCaveat,
    LookupResourcesRequest,
    LookupSubjectsRequest,
    ObjectReference,
    ReadSchemaRequest,
    Relationship,
    RelationshipUpdate,
    SubjectReference,
    SyncClient,
    WriteRelationshipsRequest,
    WriteSchemaRequest,
)
from .calls import write_test_schema
from .utils import maybe_async_iterable_to_list, maybe_await
from grpcutil import insecure_bearer_token_credentials


@pytest.fixture()
def client_autodetect_sync(token) -> Client:
    with pytest.raises(RuntimeError):
        asyncio.get_running_loop()
    return Client("localhost:50051", insecure_bearer_token_credentials(token))


@pytest.fixture()
async def client_autodetect_async(token) -> Client:
    assert asyncio.get_running_loop()
    return Client("localhost:50051", insecure_bearer_token_credentials(token))


@pytest.fixture()
def sync_client(token) -> SyncClient:
    return SyncClient("localhost:50051", insecure_bearer_token_credentials(token))


@pytest.fixture()
async def async_client(token) -> AsyncClient:
    return AsyncClient("localhost:50051", insecure_bearer_token_credentials(token))


# The configs array paramaterizes the tests in this file to run with different clients.
# To make changes, modify both the configs array and the config fixture
Config = Literal["Client_autodetect_sync", "Client_autodetect_async", "SyncClient", "AsyncClient"]
configs: list[Config] = [
    "Client_autodetect_sync",
    "Client_autodetect_async",
    "SyncClient",
    "AsyncClient",
]


@pytest.fixture(params=configs)
def client(
    request,
    client_autodetect_sync: Client,
    client_autodetect_async: Client,
    sync_client: SyncClient,
    async_client: AsyncClient,
):
    clients: dict[Config, Any] = {
        "Client_autodetect_sync": client_autodetect_sync,
        "Client_autodetect_async": client_autodetect_async,
        "SyncClient": sync_client,
        "AsyncClient": async_client,
    }
    return clients[request.param]


async def test_basic_schema(client):
    schema = """
        definition document {
            relation reader: user
        }
        definition user {}
    """
    resp = await maybe_await(client.WriteSchema(WriteSchemaRequest(schema=schema)))
    resp = await maybe_await(client.ReadSchema(ReadSchemaRequest()))
    assert "definition document" in resp.schema_text
    assert "definition user" in resp.schema_text


async def test_schema_with_caveats(client):
    await write_test_schema(client)


async def test_check(client):
    # Write a basic schema.
    await write_test_schema(client)
    beatrice, emilia, post_one, post_two = await write_test_tuples(client)

    # Issue some checks.
    resp = await maybe_await(
        client.CheckPermission(
            CheckPermissionRequest(
                resource=post_one,
                permission="view",
                subject=emilia,
                consistency=Consistency(fully_consistent=True),
            )
        )
    )
    assert resp.permissionship == CheckPermissionResponse.PERMISSIONSHIP_HAS_PERMISSION

    resp = await maybe_await(
        client.CheckPermission(
            CheckPermissionRequest(
                resource=post_one,
                permission="write",
                subject=emilia,
                consistency=Consistency(fully_consistent=True),
            )
        )
    )
    assert resp.permissionship == CheckPermissionResponse.PERMISSIONSHIP_HAS_PERMISSION

    resp = await maybe_await(
        client.CheckPermission(
            CheckPermissionRequest(
                resource=post_one,
                permission="view",
                subject=beatrice,
                consistency=Consistency(fully_consistent=True),
            )
        )
    )
    assert resp.permissionship == CheckPermissionResponse.PERMISSIONSHIP_HAS_PERMISSION

    resp = await maybe_await(
        client.CheckPermission(
            CheckPermissionRequest(
                resource=post_one,
                permission="write",
                subject=beatrice,
                consistency=Consistency(fully_consistent=True),
            )
        )
    )
    assert resp.permissionship == CheckPermissionResponse.PERMISSIONSHIP_NO_PERMISSION


async def test_caveated_check(client):
    # Write a basic schema.
    await write_test_schema(client)
    beatrice, emilia, post_one, post_two = await write_test_tuples(client)

    s = Struct()
    # Likes Harry Potter
    s.update({"likes": True})

    req = CheckPermissionRequest(
        resource=post_one,
        permission="view_as_fan",
        subject=beatrice,
        consistency=Consistency(fully_consistent=True),
        context=s,
    )

    resp = await maybe_await(client.CheckPermission(req))
    assert resp.permissionship == CheckPermissionResponse.PERMISSIONSHIP_HAS_PERMISSION

    # No longer likes Harry Potter
    s.update({"likes": False})
    req = CheckPermissionRequest(
        resource=post_one,
        permission="view_as_fan",
        subject=beatrice,
        consistency=Consistency(fully_consistent=True),
        context=s,
    )
    resp = await maybe_await(client.CheckPermission(req))
    assert resp.permissionship == CheckPermissionResponse.PERMISSIONSHIP_NO_PERMISSION

    # Fandom is in question
    req = CheckPermissionRequest(
        resource=post_one,
        permission="view_as_fan",
        subject=beatrice,
        consistency=Consistency(fully_consistent=True),
        context=None,
    )
    resp = await maybe_await(client.CheckPermission(req))
    assert resp.permissionship == CheckPermissionResponse.PERMISSIONSHIP_CONDITIONAL_PERMISSION
    assert "likes" in resp.partial_caveat_info.missing_required_context


async def test_lookup_resources(client):
    # Write a basic schema.
    await write_test_schema(client)
    beatrice, emilia, post_one, post_two = await write_test_tuples(client)

    resp = client.LookupResources(
        LookupResourcesRequest(
            resource_object_type="post",
            permission="write",
            subject=emilia,
            consistency=Consistency(fully_consistent=True),
        )
    )
    responses = await maybe_async_iterable_to_list(resp)
    responses = [response.resource_object_id for response in responses]
    assert len(responses) == 2
    assert responses.count(post_one.object_id) == 1
    assert responses.count(post_two.object_id) == 1


async def test_lookup_subjects(client):
    # Write a basic schema.
    await write_test_schema(client)
    beatrice, emilia, post_one, post_two = await write_test_tuples(client)

    resp = client.LookupSubjects(
        LookupSubjectsRequest(
            subject_object_type="user",
            permission="view",
            resource=post_one,
            consistency=Consistency(fully_consistent=True),
        )
    )
    responses = await maybe_async_iterable_to_list(resp)
    responses = [response.subject_object_id for response in responses]
    assert len(responses) == 2
    assert responses.count(emilia.object.object_id) == 1
    assert responses.count(beatrice.object.object_id) == 1


async def test_bulk_check(client):
    # Write a basic schema.
    await write_test_schema(client)
    beatrice, emilia, post_one, post_two = await write_test_tuples(client)

    # Issue some checks.
    resp = await maybe_await(
        client.BulkCheckPermission(
            BulkCheckPermissionRequest(
                consistency=Consistency(fully_consistent=True),
                items=[
                    BulkCheckPermissionRequestItem(
                        resource=post_one,
                        permission="view",
                        subject=emilia,
                    ),
                    BulkCheckPermissionRequestItem(
                        resource=post_one,
                        permission="write",
                        subject=emilia,
                    ),
                ],
            )
        )
    )

    assert len(resp.pairs) == 2
    assert (
        resp.pairs[0].item.permissionship == CheckPermissionResponse.PERMISSIONSHIP_HAS_PERMISSION
    )
    assert (
        resp.pairs[1].item.permissionship == CheckPermissionResponse.PERMISSIONSHIP_HAS_PERMISSION
    )


async def test_bulk_export_import(client):
    await write_test_schema(client)
    await write_test_tuples(client)

    # validate bulk export returns all relationships written
    resp = client.BulkExportRelationships(
        BulkExportRelationshipsRequest(consistency=Consistency(fully_consistent=True))
    )

    rels = await rels_from_bulk_export_response(resp)
    assert len(rels) == 4

    # create a new empty client
    ClientType = type(client)
    empty_client = ClientType(
        "localhost:50051", insecure_bearer_token_credentials(str(uuid.uuid4()))
    )
    await write_test_schema(empty_client)

    # validate indeed empty client is empty
    resp = empty_client.BulkExportRelationships(
        BulkExportRelationshipsRequest(consistency=Consistency(fully_consistent=True))
    )

    no_rels = await rels_from_bulk_export_response(resp)
    assert len(no_rels) == 0

    # do bulk import
    reqs = [BulkImportRelationshipsRequest(relationships=rels)]
    import_rels = await maybe_await(empty_client.BulkImportRelationships(((req for req in reqs))))
    assert import_rels.num_loaded == 4

    # validate all relationships were imported
    resp = empty_client.BulkExportRelationships(
        BulkExportRelationshipsRequest(consistency=Consistency(fully_consistent=True))
    )
    rels = await rels_from_bulk_export_response(resp)
    assert len(rels) == 4


async def rels_from_bulk_export_response(resp):
    resp = await maybe_async_iterable_to_list(resp)
    rels = []
    for r in resp:
        rels.extend(r.relationships)
    return rels


async def write_test_tuples(client):
    emilia = SubjectReference(
        object=ObjectReference(
            object_type="user",
            object_id="emilia",
        )
    )
    beatrice = SubjectReference(
        object=ObjectReference(
            object_type="user",
            object_id="beatrice",
        )
    )
    post_one = ObjectReference(object_type="post", object_id="post-one")
    post_two = ObjectReference(object_type="post", object_id="post-two")
    # Add some relationships.
    await maybe_await(
        client.WriteRelationships(
            WriteRelationshipsRequest(
                updates=[
                    # Emilia is a Writer on Post 1
                    RelationshipUpdate(
                        operation=RelationshipUpdate.Operation.OPERATION_CREATE,
                        relationship=Relationship(
                            resource=post_one,
                            relation="writer",
                            subject=emilia,
                        ),
                    ),
                    # Emilia is a Writer on Post 2
                    RelationshipUpdate(
                        operation=RelationshipUpdate.Operation.OPERATION_CREATE,
                        relationship=Relationship(
                            resource=post_two,
                            relation="writer",
                            subject=emilia,
                        ),
                    ),
                    # Beatrice is a Reader on Post 1
                    RelationshipUpdate(
                        operation=RelationshipUpdate.Operation.OPERATION_CREATE,
                        relationship=Relationship(
                            resource=post_one,
                            relation="reader",
                            subject=beatrice,
                        ),
                    ),
                    # Beatrice is also a caveated Reader on Post 1
                    RelationshipUpdate(
                        operation=RelationshipUpdate.Operation.OPERATION_CREATE,
                        relationship=Relationship(
                            resource=post_one,
                            relation="caveated_reader",
                            subject=beatrice,
                            optional_caveat=ContextualizedCaveat(caveat_name="likes_harry_potter"),
                        ),
                    ),
                ]
            )
        )
    )
    return beatrice, emilia, post_one, post_two
