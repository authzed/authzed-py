from authzed.api.v1 import (
    BulkExportRelationshipsRequest,
    BulkImportRelationshipsRequest,
    Client,
    Consistency,
    ObjectReference,
    Relationship,
    SubjectReference,
    WriteSchemaRequest,
)
from grpcutil import insecure_bearer_token_credentials

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

client = Client(
    "localhost:50051",
    insecure_bearer_token_credentials("t_your_token_here_1234567deadbeef"),
)

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


reqs = [
    BulkImportRelationshipsRequest(
        relationships=[
            Relationship(
                resource=post_one,
                relation="reader",
                subject=emilia,
            ),
            Relationship(
                resource=post_one,
                relation="writer",
                subject=beatrice,
            ),
        ]
    )
]

import_reps = client.BulkImportRelationships(((req for req in reqs)))
assert import_reps.num_loaded == 2

export_resp = client.BulkExportRelationships(
    BulkExportRelationshipsRequest(consistency=Consistency(fully_consistent=True))
)

rels = []
for response in export_resp:
    for rel in response.relationships:
        rels.append(rel)
assert len(rels) == 2
