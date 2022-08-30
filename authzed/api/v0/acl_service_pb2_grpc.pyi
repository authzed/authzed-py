"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import abc
import authzed.api.v0.acl_service_pb2
import grpc

class ACLServiceStub:
    def __init__(self, channel: grpc.Channel) -> None: ...
    Read: grpc.UnaryUnaryMultiCallable[
        authzed.api.v0.acl_service_pb2.ReadRequest,
        authzed.api.v0.acl_service_pb2.ReadResponse]

    Write: grpc.UnaryUnaryMultiCallable[
        authzed.api.v0.acl_service_pb2.WriteRequest,
        authzed.api.v0.acl_service_pb2.WriteResponse]

    Check: grpc.UnaryUnaryMultiCallable[
        authzed.api.v0.acl_service_pb2.CheckRequest,
        authzed.api.v0.acl_service_pb2.CheckResponse]

    ContentChangeCheck: grpc.UnaryUnaryMultiCallable[
        authzed.api.v0.acl_service_pb2.ContentChangeCheckRequest,
        authzed.api.v0.acl_service_pb2.CheckResponse]

    Expand: grpc.UnaryUnaryMultiCallable[
        authzed.api.v0.acl_service_pb2.ExpandRequest,
        authzed.api.v0.acl_service_pb2.ExpandResponse]

    Lookup: grpc.UnaryUnaryMultiCallable[
        authzed.api.v0.acl_service_pb2.LookupRequest,
        authzed.api.v0.acl_service_pb2.LookupResponse]


class ACLServiceServicer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def Read(self,
        request: authzed.api.v0.acl_service_pb2.ReadRequest,
        context: grpc.ServicerContext,
    ) -> authzed.api.v0.acl_service_pb2.ReadResponse: ...

    @abc.abstractmethod
    def Write(self,
        request: authzed.api.v0.acl_service_pb2.WriteRequest,
        context: grpc.ServicerContext,
    ) -> authzed.api.v0.acl_service_pb2.WriteResponse: ...

    @abc.abstractmethod
    def Check(self,
        request: authzed.api.v0.acl_service_pb2.CheckRequest,
        context: grpc.ServicerContext,
    ) -> authzed.api.v0.acl_service_pb2.CheckResponse: ...

    @abc.abstractmethod
    def ContentChangeCheck(self,
        request: authzed.api.v0.acl_service_pb2.ContentChangeCheckRequest,
        context: grpc.ServicerContext,
    ) -> authzed.api.v0.acl_service_pb2.CheckResponse: ...

    @abc.abstractmethod
    def Expand(self,
        request: authzed.api.v0.acl_service_pb2.ExpandRequest,
        context: grpc.ServicerContext,
    ) -> authzed.api.v0.acl_service_pb2.ExpandResponse: ...

    @abc.abstractmethod
    def Lookup(self,
        request: authzed.api.v0.acl_service_pb2.LookupRequest,
        context: grpc.ServicerContext,
    ) -> authzed.api.v0.acl_service_pb2.LookupResponse: ...


def add_ACLServiceServicer_to_server(servicer: ACLServiceServicer, server: grpc.Server) -> None: ...
