# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: authzed/api/v1alpha1/watchresources_service.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import google.api.annotations_pb2
import validate.validate_pb2
import authzed.api.v1.core_pb2
import authzed.api.v1alpha1.watchresources_service_pb2


class WatchResourcesServiceBase(abc.ABC):

    @abc.abstractmethod
    async def WatchResources(self, stream: 'grpclib.server.Stream[authzed.api.v1alpha1.watchresources_service_pb2.WatchResourcesRequest, authzed.api.v1alpha1.watchresources_service_pb2.WatchResourcesResponse]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/authzed.api.v1alpha1.WatchResourcesService/WatchResources': grpclib.const.Handler(
                self.WatchResources,
                grpclib.const.Cardinality.UNARY_STREAM,
                authzed.api.v1alpha1.watchresources_service_pb2.WatchResourcesRequest,
                authzed.api.v1alpha1.watchresources_service_pb2.WatchResourcesResponse,
            ),
        }


class WatchResourcesServiceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.WatchResources = grpclib.client.UnaryStreamMethod(
            channel,
            '/authzed.api.v1alpha1.WatchResourcesService/WatchResources',
            authzed.api.v1alpha1.watchresources_service_pb2.WatchResourcesRequest,
            authzed.api.v1alpha1.watchresources_service_pb2.WatchResourcesResponse,
        )
