from authzed.api.v1 import Client, WriteSchemaRequest
from grpcutil import bearer_token_credentials

SCHEMA = """definition blog/user {}

definition blog/post {
    relation reader: blog/user
    relation writer: blog/user

    permission read = reader + writer
    permission write = writer
}"""

client = Client(
    "grpc.authzed.com:443",
    bearer_token_credentials("t_your_token_here_1234567deadbeef"),
)

resp = client.WriteSchema(WriteSchemaRequest(schema=SCHEMA))
