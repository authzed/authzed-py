# Authzed Python Client

This repository houses the Python client library for Authzed.

The library maintains various versions the Authzed gRPC APIs.
You can find more info on each API on the [Authzed API reference documentation].
Additionally, Protobuf API documentation can be found on the [Buf Registry Authzed API repository].

[Authzed API Reference documentation]: https://docs.authzed.com/reference/api
[Buf Registry Authzed API repository]: https://buf.build/authzed/api/docs/main

Supported API versions:
- v1alpha1
- v0
- arrakisclient (v0 Legacy ORM)

## Installation

```
pip install authzed
```

## Example

Everything API specific is in its respective `authzed.api.VERSION` module.
`grpcutil` contains functionality for making interacting with gRPC simple.

```python
from authzed.api.v1alpha1 import Client, ReadSchemaRequest
from grpcutil import bearer_token_credentials


client = Client("grpc.authzed.com:443", bearer_token_credentials("mytoken"))
resp = client.ReadSchema(ReadSchemaRequest(object_definitions_names=["example/user"]))
print(resp.object_definitions)
```

If an event loop is running when the client is initialized, all functions calls are async:

```python
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
```

## Full Examples

Full examples for each version of the API can be found in the [examples directory](examples).
