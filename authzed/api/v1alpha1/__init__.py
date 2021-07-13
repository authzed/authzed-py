import asyncio

import grpc
import grpc.aio

from authzed.api.v1alpha1.schema_pb2 import ReadSchemaRequest, ReadSchemaResponse
from authzed.api.v1alpha1.schema_pb2_grpc import SchemaServiceStub


class Client(SchemaServiceStub):
    """
    v1alpha1 Authzed gRPC API client.
    """

    def __init__(self, target, credentials, options=None, compression=None):
        channelfn = (
            grpc.aio.secure_channel
            if asyncio.get_event_loop().is_running()
            else grpc.secure_channel
        )
        channel = channelfn(target, credentials, options, compression)
        SchemaServiceStub.__init__(self, channel)


__all__ = [
    "Client",
    "ReadSchemaRequest",
    "ReadSchemaResponse",
]
