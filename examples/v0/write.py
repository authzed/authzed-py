""" v0 API is deprecated """
from authzed.api.v0 import (
    Client,
    ObjectAndRelation,
    RelationTuple,
    RelationTupleUpdate,
    User,
    WriteRequest,
)
from grpcutil import bearer_token_credentials

client = Client("grpc.authzed.com:443", bearer_token_credentials("mytoken"))
resp = client.Write(
    WriteRequest(
        updates=[
            # Emilia is a Writer on Post 1
            RelationTupleUpdate(
                operation=RelationTupleUpdate.Operation.CREATE,
                tuple=RelationTuple(
                    user=User(namespace="blog/user", object_id="emilia"),
                    object_and_relation=ObjectAndRelation(
                        namespace="blog/post",
                        object_id="1",
                        relation="writer",
                    ),
                ),
            ),
            # Beatrice is a Reader on Post 1
            RelationTupleUpdate(
                operation=RelationTupleUpdate.Operation.CREATE,
                tuple=RelationTuple(
                    user=User(namespace="blog/user", object_id="beatrice"),
                    object_and_relation=ObjectAndRelation(
                        namespace="blog/post",
                        object_id="1",
                        relation="reader",
                    ),
                ),
            ),
        ]
    )
)
