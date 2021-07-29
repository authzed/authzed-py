from authzed.api.v1alpha1 import Client, ReadSchemaRequest
from grpcutil import bearer_token_credentials

client = Client("grpc.authzed.com:443", bearer_token_credentials("mytoken"))
resp = client.ReadSchema(ReadSchemaRequest(object_definitions_names=["example/user"]))
print(resp.object_definitions)
