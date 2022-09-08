import uuid

import pytest

from authzed.api.v1 import (
    CheckPermissionRequest,
    CheckPermissionResponse,
    Client,
    Consistency,
    LookupResourcesRequest,
    ObjectReference,
    ReadSchemaRequest,
    Relationship,
    RelationshipUpdate,
    SubjectReference,
    WriteRelationshipsRequest,
    WriteSchemaRequest,
)
from grpcutil import insecure_bearer_token_credentials


@pytest.fixture(scope="function")
def token():
    return str(uuid.uuid4())


@pytest.fixture(scope="function")
def client(token):
    # NOTE: `spicedb serve-testing` must be running for these tests to work.
    return Client("localhost:50051", insecure_bearer_token_credentials(token))


def test_basic_schema(client):
    schema = """
        definition document {
            relation reader: user
        }
        definition user {}
    """
    client.WriteSchema(WriteSchemaRequest(schema=schema))

    resp = client.ReadSchema(ReadSchemaRequest())
    assert "definition document" in resp.schema_text
    assert "definition user" in resp.schema_text


def test_check(client):
    # Write a basic schema.
    write_test_schema(client)
    beatrice, emilia, post_one, post_two = write_test_tuples(client)

    # Issue some checks.
    resp = client.CheckPermission(
        CheckPermissionRequest(
            resource=post_one,
            permission="view",
            subject=emilia,
            consistency=Consistency(fully_consistent=True),
        )
    )
    assert resp.permissionship == CheckPermissionResponse.PERMISSIONSHIP_HAS_PERMISSION

    resp = client.CheckPermission(
        CheckPermissionRequest(
            resource=post_one,
            permission="write",
            subject=emilia,
            consistency=Consistency(fully_consistent=True),
        )
    )
    assert resp.permissionship == CheckPermissionResponse.PERMISSIONSHIP_HAS_PERMISSION

    resp = client.CheckPermission(
        CheckPermissionRequest(
            resource=post_one,
            permission="view",
            subject=beatrice,
            consistency=Consistency(fully_consistent=True),
        )
    )
    assert resp.permissionship == CheckPermissionResponse.PERMISSIONSHIP_HAS_PERMISSION

    resp = client.CheckPermission(
        CheckPermissionRequest(
            resource=post_one,
            permission="write",
            subject=beatrice,
            consistency=Consistency(fully_consistent=True),
        )
    )
    assert resp.permissionship == CheckPermissionResponse.PERMISSIONSHIP_NO_PERMISSION


def test_lookup_resources(client):
    # Write a basic schema.
    write_test_schema(client)
    beatrice, emilia, post_one, post_two = write_test_tuples(client)

    resp = client.LookupResources(
        LookupResourcesRequest(
            resource_object_type="post",
            permission="write",
            subject=emilia,
            consistency=Consistency(fully_consistent=True),
        )
    )
    responses = []
    for response in resp:
        responses.append(response.resource_object_id)
    assert len(responses) == 2
    assert responses.count(post_one.object_id) == 1
    assert responses.count(post_two.object_id) == 1


# def test_lookup_subjects(client):
#     # Write a basic schema.
#     write_test_schema(client)
#     beatrice, emilia, post_one, post_two = write_test_tuples(client)
#
#     resp = client.LookupSubjects(
#         LookupSubjectsRequest(
#             subject_object_type="user",
#             permission="view",
#             resource=post_one,
#             consistency=Consistency(fully_consistent=True),
#         )
#     )
#     responses = []
#     for response in resp:
#         responses.append(response.subject_object_id)
#     assert len(responses) == 2
#     assert responses.count(emilia.object.object_id) == 1
#     assert responses.count(beatrice.object.object_id) == 1


def write_test_tuples(client):
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
            ]
        )
    )
    return beatrice, emilia, post_one, post_two


def write_test_schema(client):
    schema = """
        definition post {
            relation writer: user
            relation reader: user

            permission write = writer
            permission view = reader + writer
        }
        definition user {}
    """
    client.WriteSchema(WriteSchemaRequest(schema=schema))
