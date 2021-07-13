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
- v0 ORM (arrakisclient)

## Quick Example - v1alpha1

```
pip install authzed
```

```python
from authzed.api.v1alpha1 import Client, SchemaRequest
from authzed.api.v1alpha1.grpcutil import bearer_token_credentials

client = Client("grpc.authzed.com:443", bearer_token_credentials("mytoken"))
resp = client.ReadSchema(ReadSchemaRequest(object_definitions_names=["example/user"]))
print(resp.object_definitions)
```

## Full Examples

Full examples for each version of the API can be found in the [examples directory](examples).
