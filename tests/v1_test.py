import uuid

import pytest

from authzed.api.v1 import (
    CheckPermissionRequest,
    CheckPermissionResponse,
    Client,
    Consistency,
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
    SCHEMA = """
        definition document {
            relation reader: user
        }
        definition user {}
    """
    client.WriteSchema(WriteSchemaRequest(schema=SCHEMA))

    resp = client.ReadSchema(ReadSchemaRequest())
    assert "definition document" in resp.schema_text
    assert "definition user" in resp.schema_text


def test_basic_operations(client):
    # Write a basic schema.
    SCHEMA = """
        definition post {
            relation writer: user
            relation reader: user

            permission write = writer
            permission view = reader + writer
        }
        definition user {}
    """
    client.WriteSchema(WriteSchemaRequest(schema=SCHEMA))

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

    post_one = ObjectReference(object_type="post", object_id="1")

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
