import asyncio

import grpc
import grpc.aio

from authzed.api.v1alpha1.schema_pb2 import (
    ReadSchemaRequest,
    ReadSchemaResponse,
    WriteSchemaRequest,
    WriteSchemaResponse,
)
from authzed.api.v1alpha1.schema_pb2_grpc import SchemaServiceStub


class Client(SchemaServiceStub):
    """
    v1alpha1 Authzed gRPC API client.
    """

    def __init__(self, target, credentials, options=None, compression=None):
        try:
            asyncio.get_running_loop()
            channelfn = grpc.aio.secure_channel
        except RuntimeError:
            channelfn = grpc.secure_channel

        channel = channelfn(target, credentials, options, compression)
        SchemaServiceStub.__init__(self, channel)


__all__ = [
    "Client",
    # Schema Service
    "ReadSchemaRequest",
    "ReadSchemaResponse",
    "WriteSchemaRequest",
    "WriteSchemaResponse",
]
