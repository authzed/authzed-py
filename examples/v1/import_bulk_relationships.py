"""
This is intended to be a (slightly) more real-world example
that demonstrates the two levels of batching in making BulkImportRelationships
requests.
"""
from itertools import batched
from authzed.api.v1 import (
    Client,
    ObjectReference,
    Relationship,
    SubjectReference,
    WriteSchemaRequest,
)
from authzed.api.v1.permission_service_pb2 import ImportBulkRelationshipsRequest
from grpcutil import insecure_bearer_token_credentials

TOKEN = "sometoken"

# Stand up a client
client = Client(
    "localhost:50051",
    insecure_bearer_token_credentials(TOKEN),
)

# Write a simple schema
schema = """
    definition user {}
    definition resource {
        relation viewer: user
        permission view = viewer
    }
"""

client.WriteSchema(WriteSchemaRequest(schema=schema))

# A generator that we can use to create an arbitrarily-long list of relationships
# In your own application, this would be whatever's generating the list of imported
# relationships.
def relationship_generator(num_relationships):
    idx = 0
    while idx < num_relationships:
        idx += 1
        yield Relationship(
            resource=ObjectReference(object_type="resource", object_id=str(idx)),
            relation="viewer",
            subject=SubjectReference(
                object=ObjectReference(object_type="user", object_id="our_user")
            ),
        )


TOTAL_RELATIONSHIPS_TO_WRITE = 1_000

RELATIONSHIPS_PER_TRANSACTION = 100
RELATIONSHIPS_PER_REQUEST_CHUNK = 10

# NOTE: batched takes a larger iterator and makes an iterator of smaller chunks out of it.
# We iterate over chunks of size RELATIONSHIPS_PER_TRANSACTION, and then we break each request into
# chunks of size RELATIONSHIPS_PER_REQUEST_CHUNK.
for relationships_for_request in batched(
    relationship_generator(TOTAL_RELATIONSHIPS_TO_WRITE), RELATIONSHIPS_PER_TRANSACTION
):
    response = client.ImportBulkRelationships(
        (
            ImportBulkRelationshipsRequest(relationships=relationships_for_chunk)
            for relationships_for_chunk in batched(
                relationships_for_request, RELATIONSHIPS_PER_REQUEST_CHUNK
            )
        )
    )
    print("request successful")
    print(response.num_loaded)
