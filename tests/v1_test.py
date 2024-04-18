import uuid

import pytest
from google.protobuf.struct_pb2 import Struct
import asyncio
from typing import Literal, Any
from dataclasses import dataclass

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
from grpcutil import insecure_bearer_token_credentials


# The Configuration class paramaterizes the tests in this file to run with different clients.
# To make changes, Modify the dataclass, and the client fixture
@dataclass
class Configuration:
    Client_autodetect_sync: Literal["sync", "async"] = "sync"
    Client_autodetect_async: Literal["sync", "async"] = "async"
    SyncClient: Literal["sync", "async"] = "sync"
    AsyncClient: Literal["sync", "async"] = "async"


@pytest.fixture(
    params=Configuration().__dict__.items(),
    ids=list(Configuration().__dict__.keys()),
)
def client_config(request) -> tuple[str, Literal["sync", "async"]]:
    return request.param


@pytest.fixture()
def is_async(client_config: tuple[str, Literal["sync", "async"]]) -> bool:
    return client_config[1] == "async"


@pytest.fixture()
def token():
    return str(uuid.uuid4())


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


@pytest.fixture()
def client(
    client_config: tuple[str, Literal["sync", "async"]],
    client_autodetect_sync: Client,
    client_autodetect_async: Client,
    sync_client: SyncClient,
    async_client: AsyncClient,
):
    clients = {
        "Client_autodetect_sync": client_autodetect_sync,
        "Client_autodetect_async": client_autodetect_async,
        "SyncClient": sync_client,
        "AsyncClient": async_client,
    }
    return clients[client_config[0]]


async def test_basic_schema(client, is_async: bool):
    schema = """
        definition document {
            relation reader: user
        }
        definition user {}
    """
    resp = client.WriteSchema(WriteSchemaRequest(schema=schema))
    if is_async:
        await resp

    resp = client.ReadSchema(ReadSchemaRequest())
    if is_async:
        resp = await resp
    assert "definition document" in resp.schema_text
    assert "definition user" in resp.schema_text


async def test_schema_with_caveats(client, is_async: bool):
    await write_test_schema(client, is_async=is_async)


async def test_check(client, is_async: bool):
    # Write a basic schema.
    await write_test_schema(client, is_async=is_async)
    beatrice, emilia, post_one, post_two = await write_test_tuples(client, is_async=is_async)

    # Issue some checks.
    resp = client.CheckPermission(
        CheckPermissionRequest(
            resource=post_one,
            permission="view",
            subject=emilia,
            consistency=Consistency(fully_consistent=True),
        )
    )
    if is_async:
        resp = await resp
    assert resp.permissionship == CheckPermissionResponse.PERMISSIONSHIP_HAS_PERMISSION

    resp = client.CheckPermission(
        CheckPermissionRequest(
            resource=post_one,
            permission="write",
            subject=emilia,
            consistency=Consistency(fully_consistent=True),
        )
    )
    if is_async:
        resp = await resp
    assert resp.permissionship == CheckPermissionResponse.PERMISSIONSHIP_HAS_PERMISSION

    resp = client.CheckPermission(
        CheckPermissionRequest(
            resource=post_one,
            permission="view",
            subject=beatrice,
            consistency=Consistency(fully_consistent=True),
        )
    )
    if is_async:
        resp = await resp
    assert resp.permissionship == CheckPermissionResponse.PERMISSIONSHIP_HAS_PERMISSION

    resp = client.CheckPermission(
        CheckPermissionRequest(
            resource=post_one,
            permission="write",
            subject=beatrice,
            consistency=Consistency(fully_consistent=True),
        )
    )
    if is_async:
        resp = await resp
    assert resp.permissionship == CheckPermissionResponse.PERMISSIONSHIP_NO_PERMISSION


async def test_caveated_check(client, is_async: bool):
    # Write a basic schema.
    await write_test_schema(client, is_async=is_async)
    beatrice, emilia, post_one, post_two = await write_test_tuples(client, is_async=is_async)

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

    resp = client.CheckPermission(req)
    if is_async:
        resp = await resp
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
    resp = client.CheckPermission(req)
    if is_async:
        resp = await resp
    assert resp.permissionship == CheckPermissionResponse.PERMISSIONSHIP_NO_PERMISSION

    # Fandom is in question
    req = CheckPermissionRequest(
        resource=post_one,
        permission="view_as_fan",
        subject=beatrice,
        consistency=Consistency(fully_consistent=True),
        context=None,
    )
    resp = client.CheckPermission(req)
    if is_async:
        resp = await resp
    assert resp.permissionship == CheckPermissionResponse.PERMISSIONSHIP_CONDITIONAL_PERMISSION
    assert "likes" in resp.partial_caveat_info.missing_required_context


async def test_lookup_resources(client, is_async: bool):
    # Write a basic schema.
    await write_test_schema(client, is_async=is_async)
    beatrice, emilia, post_one, post_two = await write_test_tuples(client, is_async=is_async)

    resp = client.LookupResources(
        LookupResourcesRequest(
            resource_object_type="post",
            permission="write",
            subject=emilia,
            consistency=Consistency(fully_consistent=True),
        )
    )
    responses = []
    if is_async:
        async for response in resp:
            responses.append(response.resource_object_id)
    else:
        for response in resp:
            responses.append(response.resource_object_id)
    assert len(responses) == 2
    assert responses.count(post_one.object_id) == 1
    assert responses.count(post_two.object_id) == 1


async def test_lookup_subjects(client, is_async: bool):
    # Write a basic schema.
    await write_test_schema(client, is_async=is_async)
    beatrice, emilia, post_one, post_two = await write_test_tuples(client, is_async=is_async)

    resp = client.LookupSubjects(
        LookupSubjectsRequest(
            subject_object_type="user",
            permission="view",
            resource=post_one,
            consistency=Consistency(fully_consistent=True),
        )
    )
    responses = []
    if is_async:
        async for response in resp:
            responses.append(response.subject_object_id)
    else:
        for response in resp:
            responses.append(response.subject_object_id)
    assert len(responses) == 2
    assert responses.count(emilia.object.object_id) == 1
    assert responses.count(beatrice.object.object_id) == 1


async def test_bulk_check(client, is_async: bool):
    # Write a basic schema.
    await write_test_schema(client, is_async=is_async)
    beatrice, emilia, post_one, post_two = await write_test_tuples(client, is_async=is_async)

    # Issue some checks.
    resp = client.BulkCheckPermission(
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
    if is_async:
        resp = await resp

    assert len(resp.pairs) == 2
    assert (
        resp.pairs[0].item.permissionship == CheckPermissionResponse.PERMISSIONSHIP_HAS_PERMISSION
    )
    assert (
        resp.pairs[1].item.permissionship == CheckPermissionResponse.PERMISSIONSHIP_HAS_PERMISSION
    )


async def test_bulk_export_import(client, is_async: bool):
    await write_test_schema(client, is_async=is_async)
    await write_test_tuples(client, is_async=is_async)

    # validate bulk export returns all relationships written
    resp = client.BulkExportRelationships(
        BulkExportRelationshipsRequest(consistency=Consistency(fully_consistent=True))
    )

    rels = await rels_from_bulk_export_response(resp, is_async=is_async)
    assert len(rels) == 4

    # create a new empty client

    if is_async:
        empty_client = AsyncClient(
            "localhost:50051", insecure_bearer_token_credentials(str(uuid.uuid4()))
        )
    else:
        empty_client = SyncClient(
            "localhost:50051", insecure_bearer_token_credentials(str(uuid.uuid4()))
        )
    await write_test_schema(empty_client, is_async=is_async)

    # validate indeed empty client is empty
    resp = empty_client.BulkExportRelationships(
        BulkExportRelationshipsRequest(consistency=Consistency(fully_consistent=True))
    )

    no_rels = await rels_from_bulk_export_response(resp, is_async=is_async)
    assert len(no_rels) == 0

    # do bulk import
    reqs = [BulkImportRelationshipsRequest(relationships=rels)]
    import_rels = empty_client.BulkImportRelationships(((req for req in reqs)))
    if is_async:
        import_rels = await import_rels
    assert import_rels.num_loaded == 4

    # validate all relationships were imported
    resp = empty_client.BulkExportRelationships(
        BulkExportRelationshipsRequest(consistency=Consistency(fully_consistent=True))
    )
    rels = await rels_from_bulk_export_response(resp, is_async=is_async)
    assert len(rels) == 4


async def rels_from_bulk_export_response(resp, *, is_async: bool):
    rels = []
    if is_async:
        async for response in resp:
            for rel in response.relationships:
                rels.append(rel)
    else:
        for response in resp:
            for rel in response.relationships:
                rels.append(rel)
    return rels


async def write_test_tuples(client, *, is_async: bool):
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
    resp = client.WriteRelationships(
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
    if is_async:
        resp = await resp
    return beatrice, emilia, post_one, post_two


async def write_test_schema(client, *, is_async: bool):
    schema = """
        caveat likes_harry_potter(likes bool) {
          likes == true
        }

        definition post {
            relation writer: user
            relation reader: user
            relation caveated_reader: user with likes_harry_potter

            permission write = writer
            permission view = reader + writer
            permission view_as_fan = caveated_reader + writer
        }
        definition user {}
    """
    resp = client.WriteSchema(WriteSchemaRequest(schema=schema))
    if is_async:
        await resp
