# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: authzed/api/v1alpha1/schema.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import validate.validate_pb2
import authzed.api.v1alpha1.schema_pb2


class SchemaServiceBase(abc.ABC):

    @abc.abstractmethod
    async def ReadSchema(self, stream: 'grpclib.server.Stream[authzed.api.v1alpha1.schema_pb2.ReadSchemaRequest, authzed.api.v1alpha1.schema_pb2.ReadSchemaResponse]') -> None:
        pass

    @abc.abstractmethod
    async def WriteSchema(self, stream: 'grpclib.server.Stream[authzed.api.v1alpha1.schema_pb2.WriteSchemaRequest, authzed.api.v1alpha1.schema_pb2.WriteSchemaResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/authzed.api.v1alpha1.SchemaService/ReadSchema': grpclib.const.Handler(
                self.ReadSchema,
                grpclib.const.Cardinality.UNARY_UNARY,
                authzed.api.v1alpha1.schema_pb2.ReadSchemaRequest,
                authzed.api.v1alpha1.schema_pb2.ReadSchemaResponse,
            ),
            '/authzed.api.v1alpha1.SchemaService/WriteSchema': grpclib.const.Handler(
                self.WriteSchema,
                grpclib.const.Cardinality.UNARY_UNARY,
                authzed.api.v1alpha1.schema_pb2.WriteSchemaRequest,
                authzed.api.v1alpha1.schema_pb2.WriteSchemaResponse,
            ),
        }


class SchemaServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.ReadSchema = grpclib.client.UnaryUnaryMethod(
            channel,
            '/authzed.api.v1alpha1.SchemaService/ReadSchema',
            authzed.api.v1alpha1.schema_pb2.ReadSchemaRequest,
            authzed.api.v1alpha1.schema_pb2.ReadSchemaResponse,
        )
        self.WriteSchema = grpclib.client.UnaryUnaryMethod(
            channel,
            '/authzed.api.v1alpha1.SchemaService/WriteSchema',
            authzed.api.v1alpha1.schema_pb2.WriteSchemaRequest,
            authzed.api.v1alpha1.schema_pb2.WriteSchemaResponse,
        )
