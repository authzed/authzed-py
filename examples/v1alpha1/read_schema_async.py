import asyncio

from authzed.api.v1alpha1 import Client, ReadSchemaRequest
from grpcutil import bearer_token_credentials


async def async_new_client():
    # Within an async context, the client's methods are all async:
    client = Client("grpc.authzed.com:443", bearer_token_credentials("mytoken"))
    resp = await client.ReadSchema(ReadSchemaRequest(object_definitions_names=["example/user"]))
    print(resp)


loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(async_new_client())
finally:
    loop.close()
