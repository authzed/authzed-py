"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import authzed.api.v1.schema_service_pb2
import grpc

class SchemaServiceStub:
    """SchemaService implements operations on a Permissions System's Schema."""

    def __init__(self, channel: grpc.Channel) -> None: ...
    ReadSchema: grpc.UnaryUnaryMultiCallable[
        authzed.api.v1.schema_service_pb2.ReadSchemaRequest,
        authzed.api.v1.schema_service_pb2.ReadSchemaResponse,
    ]
    """Read returns the current Object Definitions for a Permissions System.

    Errors include:
    - INVALID_ARGUMENT: a provided value has failed to semantically validate
    - NOT_FOUND: no schema has been defined
    """
    WriteSchema: grpc.UnaryUnaryMultiCallable[
        authzed.api.v1.schema_service_pb2.WriteSchemaRequest,
        authzed.api.v1.schema_service_pb2.WriteSchemaResponse,
    ]
    """Write overwrites the current Object Definitions for a Permissions System."""

class SchemaServiceServicer(metaclass=abc.ABCMeta):
    """SchemaService implements operations on a Permissions System's Schema."""

    @abc.abstractmethod
    def ReadSchema(
        self,
        request: authzed.api.v1.schema_service_pb2.ReadSchemaRequest,
        context: grpc.ServicerContext,
    ) -> authzed.api.v1.schema_service_pb2.ReadSchemaResponse:
        """Read returns the current Object Definitions for a Permissions System.

        Errors include:
        - INVALID_ARGUMENT: a provided value has failed to semantically validate
        - NOT_FOUND: no schema has been defined
        """
    @abc.abstractmethod
    def WriteSchema(
        self,
        request: authzed.api.v1.schema_service_pb2.WriteSchemaRequest,
        context: grpc.ServicerContext,
    ) -> authzed.api.v1.schema_service_pb2.WriteSchemaResponse:
        """Write overwrites the current Object Definitions for a Permissions System."""

def add_SchemaServiceServicer_to_server(servicer: SchemaServiceServicer, server: grpc.Server) -> None: ...
