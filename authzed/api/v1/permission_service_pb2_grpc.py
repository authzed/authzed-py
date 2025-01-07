# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from authzed.api.v1 import permission_service_pb2 as authzed_dot_api_dot_v1_dot_permission__service__pb2


class PermissionsServiceStub(object):
    """PermissionsService implements a set of RPCs that perform operations on
    relationships and permissions.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ReadRelationships = channel.unary_stream(
                '/authzed.api.v1.PermissionsService/ReadRelationships',
                request_serializer=authzed_dot_api_dot_v1_dot_permission__service__pb2.ReadRelationshipsRequest.SerializeToString,
                response_deserializer=authzed_dot_api_dot_v1_dot_permission__service__pb2.ReadRelationshipsResponse.FromString,
                )
        self.WriteRelationships = channel.unary_unary(
                '/authzed.api.v1.PermissionsService/WriteRelationships',
                request_serializer=authzed_dot_api_dot_v1_dot_permission__service__pb2.WriteRelationshipsRequest.SerializeToString,
                response_deserializer=authzed_dot_api_dot_v1_dot_permission__service__pb2.WriteRelationshipsResponse.FromString,
                )
        self.DeleteRelationships = channel.unary_unary(
                '/authzed.api.v1.PermissionsService/DeleteRelationships',
                request_serializer=authzed_dot_api_dot_v1_dot_permission__service__pb2.DeleteRelationshipsRequest.SerializeToString,
                response_deserializer=authzed_dot_api_dot_v1_dot_permission__service__pb2.DeleteRelationshipsResponse.FromString,
                )
        self.CheckPermission = channel.unary_unary(
                '/authzed.api.v1.PermissionsService/CheckPermission',
                request_serializer=authzed_dot_api_dot_v1_dot_permission__service__pb2.CheckPermissionRequest.SerializeToString,
                response_deserializer=authzed_dot_api_dot_v1_dot_permission__service__pb2.CheckPermissionResponse.FromString,
                )
        self.CheckBulkPermissions = channel.unary_unary(
                '/authzed.api.v1.PermissionsService/CheckBulkPermissions',
                request_serializer=authzed_dot_api_dot_v1_dot_permission__service__pb2.CheckBulkPermissionsRequest.SerializeToString,
                response_deserializer=authzed_dot_api_dot_v1_dot_permission__service__pb2.CheckBulkPermissionsResponse.FromString,
                )
        self.ExpandPermissionTree = channel.unary_unary(
                '/authzed.api.v1.PermissionsService/ExpandPermissionTree',
                request_serializer=authzed_dot_api_dot_v1_dot_permission__service__pb2.ExpandPermissionTreeRequest.SerializeToString,
                response_deserializer=authzed_dot_api_dot_v1_dot_permission__service__pb2.ExpandPermissionTreeResponse.FromString,
                )
        self.LookupResources = channel.unary_stream(
                '/authzed.api.v1.PermissionsService/LookupResources',
                request_serializer=authzed_dot_api_dot_v1_dot_permission__service__pb2.LookupResourcesRequest.SerializeToString,
                response_deserializer=authzed_dot_api_dot_v1_dot_permission__service__pb2.LookupResourcesResponse.FromString,
                )
        self.LookupSubjects = channel.unary_stream(
                '/authzed.api.v1.PermissionsService/LookupSubjects',
                request_serializer=authzed_dot_api_dot_v1_dot_permission__service__pb2.LookupSubjectsRequest.SerializeToString,
                response_deserializer=authzed_dot_api_dot_v1_dot_permission__service__pb2.LookupSubjectsResponse.FromString,
                )
        self.ImportBulkRelationships = channel.stream_unary(
                '/authzed.api.v1.PermissionsService/ImportBulkRelationships',
                request_serializer=authzed_dot_api_dot_v1_dot_permission__service__pb2.ImportBulkRelationshipsRequest.SerializeToString,
                response_deserializer=authzed_dot_api_dot_v1_dot_permission__service__pb2.ImportBulkRelationshipsResponse.FromString,
                )
        self.ExportBulkRelationships = channel.unary_stream(
                '/authzed.api.v1.PermissionsService/ExportBulkRelationships',
                request_serializer=authzed_dot_api_dot_v1_dot_permission__service__pb2.ExportBulkRelationshipsRequest.SerializeToString,
                response_deserializer=authzed_dot_api_dot_v1_dot_permission__service__pb2.ExportBulkRelationshipsResponse.FromString,
                )


class PermissionsServiceServicer(object):
    """PermissionsService implements a set of RPCs that perform operations on
    relationships and permissions.
    """

    def ReadRelationships(self, request, context):
        """ReadRelationships reads a set of the relationships matching one or more
        filters.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WriteRelationships(self, request, context):
        """WriteRelationships atomically writes and/or deletes a set of specified
        relationships. An optional set of preconditions can be provided that must
        be satisfied for the operation to commit.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteRelationships(self, request, context):
        """DeleteRelationships atomically bulk deletes all relationships matching the
        provided filter. If no relationships match, none will be deleted and the
        operation will succeed. An optional set of preconditions can be provided that must
        be satisfied for the operation to commit.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckPermission(self, request, context):
        """CheckPermission determines for a given resource whether a subject computes
        to having a permission or is a direct member of a particular relation.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CheckBulkPermissions(self, request, context):
        """CheckBulkPermissions evaluates the given list of permission checks
        and returns the list of results.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExpandPermissionTree(self, request, context):
        """ExpandPermissionTree reveals the graph structure for a resource's
        permission or relation. This RPC does not recurse infinitely deep and may
        require multiple calls to fully unnest a deeply nested graph.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LookupResources(self, request, context):
        """LookupResources returns all the resources of a given type that a subject
        can access whether via a computed permission or relation membership.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LookupSubjects(self, request, context):
        """LookupSubjects returns all the subjects of a given type that
        have access whether via a computed permission or relation membership.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ImportBulkRelationships(self, request_iterator, context):
        """ImportBulkRelationships is a faster path to writing a large number of
        relationships at once. It is both batched and streaming. For maximum
        performance, the caller should attempt to write relationships in as close
        to relationship sort order as possible: (resource.object_type,
        resource.object_id, relation, subject.object.object_type,
        subject.object.object_id, subject.optional_relation). All relationships
        written are done so under a single transaction.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ExportBulkRelationships(self, request, context):
        """ExportBulkRelationships is the fastest path available to exporting
        relationships from the server. It is resumable, and will return results
        in an order determined by the server.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PermissionsServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ReadRelationships': grpc.unary_stream_rpc_method_handler(
                    servicer.ReadRelationships,
                    request_deserializer=authzed_dot_api_dot_v1_dot_permission__service__pb2.ReadRelationshipsRequest.FromString,
                    response_serializer=authzed_dot_api_dot_v1_dot_permission__service__pb2.ReadRelationshipsResponse.SerializeToString,
            ),
            'WriteRelationships': grpc.unary_unary_rpc_method_handler(
                    servicer.WriteRelationships,
                    request_deserializer=authzed_dot_api_dot_v1_dot_permission__service__pb2.WriteRelationshipsRequest.FromString,
                    response_serializer=authzed_dot_api_dot_v1_dot_permission__service__pb2.WriteRelationshipsResponse.SerializeToString,
            ),
            'DeleteRelationships': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteRelationships,
                    request_deserializer=authzed_dot_api_dot_v1_dot_permission__service__pb2.DeleteRelationshipsRequest.FromString,
                    response_serializer=authzed_dot_api_dot_v1_dot_permission__service__pb2.DeleteRelationshipsResponse.SerializeToString,
            ),
            'CheckPermission': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckPermission,
                    request_deserializer=authzed_dot_api_dot_v1_dot_permission__service__pb2.CheckPermissionRequest.FromString,
                    response_serializer=authzed_dot_api_dot_v1_dot_permission__service__pb2.CheckPermissionResponse.SerializeToString,
            ),
            'CheckBulkPermissions': grpc.unary_unary_rpc_method_handler(
                    servicer.CheckBulkPermissions,
                    request_deserializer=authzed_dot_api_dot_v1_dot_permission__service__pb2.CheckBulkPermissionsRequest.FromString,
                    response_serializer=authzed_dot_api_dot_v1_dot_permission__service__pb2.CheckBulkPermissionsResponse.SerializeToString,
            ),
            'ExpandPermissionTree': grpc.unary_unary_rpc_method_handler(
                    servicer.ExpandPermissionTree,
                    request_deserializer=authzed_dot_api_dot_v1_dot_permission__service__pb2.ExpandPermissionTreeRequest.FromString,
                    response_serializer=authzed_dot_api_dot_v1_dot_permission__service__pb2.ExpandPermissionTreeResponse.SerializeToString,
            ),
            'LookupResources': grpc.unary_stream_rpc_method_handler(
                    servicer.LookupResources,
                    request_deserializer=authzed_dot_api_dot_v1_dot_permission__service__pb2.LookupResourcesRequest.FromString,
                    response_serializer=authzed_dot_api_dot_v1_dot_permission__service__pb2.LookupResourcesResponse.SerializeToString,
            ),
            'LookupSubjects': grpc.unary_stream_rpc_method_handler(
                    servicer.LookupSubjects,
                    request_deserializer=authzed_dot_api_dot_v1_dot_permission__service__pb2.LookupSubjectsRequest.FromString,
                    response_serializer=authzed_dot_api_dot_v1_dot_permission__service__pb2.LookupSubjectsResponse.SerializeToString,
            ),
            'ImportBulkRelationships': grpc.stream_unary_rpc_method_handler(
                    servicer.ImportBulkRelationships,
                    request_deserializer=authzed_dot_api_dot_v1_dot_permission__service__pb2.ImportBulkRelationshipsRequest.FromString,
                    response_serializer=authzed_dot_api_dot_v1_dot_permission__service__pb2.ImportBulkRelationshipsResponse.SerializeToString,
            ),
            'ExportBulkRelationships': grpc.unary_stream_rpc_method_handler(
                    servicer.ExportBulkRelationships,
                    request_deserializer=authzed_dot_api_dot_v1_dot_permission__service__pb2.ExportBulkRelationshipsRequest.FromString,
                    response_serializer=authzed_dot_api_dot_v1_dot_permission__service__pb2.ExportBulkRelationshipsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'authzed.api.v1.PermissionsService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PermissionsService(object):
    """PermissionsService implements a set of RPCs that perform operations on
    relationships and permissions.
    """

    @staticmethod
    def ReadRelationships(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/authzed.api.v1.PermissionsService/ReadRelationships',
            authzed_dot_api_dot_v1_dot_permission__service__pb2.ReadRelationshipsRequest.SerializeToString,
            authzed_dot_api_dot_v1_dot_permission__service__pb2.ReadRelationshipsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def WriteRelationships(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/authzed.api.v1.PermissionsService/WriteRelationships',
            authzed_dot_api_dot_v1_dot_permission__service__pb2.WriteRelationshipsRequest.SerializeToString,
            authzed_dot_api_dot_v1_dot_permission__service__pb2.WriteRelationshipsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteRelationships(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/authzed.api.v1.PermissionsService/DeleteRelationships',
            authzed_dot_api_dot_v1_dot_permission__service__pb2.DeleteRelationshipsRequest.SerializeToString,
            authzed_dot_api_dot_v1_dot_permission__service__pb2.DeleteRelationshipsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CheckPermission(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/authzed.api.v1.PermissionsService/CheckPermission',
            authzed_dot_api_dot_v1_dot_permission__service__pb2.CheckPermissionRequest.SerializeToString,
            authzed_dot_api_dot_v1_dot_permission__service__pb2.CheckPermissionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CheckBulkPermissions(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/authzed.api.v1.PermissionsService/CheckBulkPermissions',
            authzed_dot_api_dot_v1_dot_permission__service__pb2.CheckBulkPermissionsRequest.SerializeToString,
            authzed_dot_api_dot_v1_dot_permission__service__pb2.CheckBulkPermissionsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ExpandPermissionTree(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/authzed.api.v1.PermissionsService/ExpandPermissionTree',
            authzed_dot_api_dot_v1_dot_permission__service__pb2.ExpandPermissionTreeRequest.SerializeToString,
            authzed_dot_api_dot_v1_dot_permission__service__pb2.ExpandPermissionTreeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LookupResources(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/authzed.api.v1.PermissionsService/LookupResources',
            authzed_dot_api_dot_v1_dot_permission__service__pb2.LookupResourcesRequest.SerializeToString,
            authzed_dot_api_dot_v1_dot_permission__service__pb2.LookupResourcesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LookupSubjects(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/authzed.api.v1.PermissionsService/LookupSubjects',
            authzed_dot_api_dot_v1_dot_permission__service__pb2.LookupSubjectsRequest.SerializeToString,
            authzed_dot_api_dot_v1_dot_permission__service__pb2.LookupSubjectsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ImportBulkRelationships(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/authzed.api.v1.PermissionsService/ImportBulkRelationships',
            authzed_dot_api_dot_v1_dot_permission__service__pb2.ImportBulkRelationshipsRequest.SerializeToString,
            authzed_dot_api_dot_v1_dot_permission__service__pb2.ImportBulkRelationshipsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ExportBulkRelationships(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/authzed.api.v1.PermissionsService/ExportBulkRelationships',
            authzed_dot_api_dot_v1_dot_permission__service__pb2.ExportBulkRelationshipsRequest.SerializeToString,
            authzed_dot_api_dot_v1_dot_permission__service__pb2.ExportBulkRelationshipsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
