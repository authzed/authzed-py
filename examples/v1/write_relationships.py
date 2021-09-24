from authzed.api.v1 import (
    Client,
    ObjectReference,
    Relationship,
    RelationshipUpdate,
    SubjectReference,
    WriteRelationshipsRequest,
)
from grpcutil import bearer_token_credentials

client = Client(
    "grpc.authzed.com:443",
    bearer_token_credentials("t_your_token_here_1234567deadbeef"),
)

resp = client.WriteRelationships(
    WriteRelationshipsRequest(
        updates=[
            # Emilia is a Writer on Post 1
            RelationshipUpdate(
                operation=RelationshipUpdate.Operation.OPERATION_CREATE,
                relationship=Relationship(
                    resource=ObjectReference(object_type="blog/post", object_id="1"),
                    relation="writer",
                    subject=SubjectReference(
                        object=ObjectReference(
                            object_type="blog/user",
                            object_id="emilia",
                        )
                    ),
                ),
            ),
            # Beatrice is a Reader on Post 1
            RelationshipUpdate(
                operation=RelationshipUpdate.Operation.OPERATION_CREATE,
                relationship=Relationship(
                    resource=ObjectReference(object_type="blog/post", object_id="1"),
                    relation="reader",
                    subject=SubjectReference(
                        object=ObjectReference(
                            object_type="blog/user",
                            object_id="beatrice",
                        )
                    ),
                ),
            ),
        ]
    )
)
