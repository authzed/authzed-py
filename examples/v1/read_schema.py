from authzed.api.v1 import Client, ReadSchemaRequest
from grpcutil import bearer_token_credentials

client = Client(
    "grpc.authzed.com:443",
    bearer_token_credentials("t_your_token_here_1234567deadbeef"),
)

resp = client.ReadSchema(ReadSchemaRequest())
print(resp.schema_text)
