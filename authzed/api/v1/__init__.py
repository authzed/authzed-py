import asyncio
from typing import Any, Callable

import grpc
import grpc.aio
from grpc_interceptor import ClientCallDetails, ClientInterceptor

from authzed.api.v1.core_pb2 import (
    AlgebraicSubjectSet,
    ContextualizedCaveat,
    Cursor,
    DirectSubjectSet,
    ObjectReference,
    PermissionRelationshipTree,
    Relationship,
    RelationshipUpdate,
    SubjectReference,
    ZedToken,
)
from authzed.api.v1.error_reason_pb2 import ErrorReason
from authzed.api.v1.experimental_service_pb2 import (
    BulkCheckPermissionPair,
    BulkCheckPermissionRequest,
    BulkCheckPermissionRequestItem,
    BulkCheckPermissionResponse,
    BulkCheckPermissionResponseItem,
    BulkExportRelationshipsRequest,
    BulkExportRelationshipsResponse,
    BulkImportRelationshipsRequest,
    BulkImportRelationshipsResponse,
)
from authzed.api.v1.experimental_service_pb2_grpc import ExperimentalServiceStub
from authzed.api.v1.permission_service_pb2 import (
    CheckBulkPermissionsPair,
    CheckBulkPermissionsRequest,
    CheckBulkPermissionsRequestItem,
    CheckBulkPermissionsResponse,
    CheckBulkPermissionsResponseItem,
    CheckPermissionRequest,
    CheckPermissionResponse,
    Consistency,
    DeleteRelationshipsRequest,
    DeleteRelationshipsResponse,
    ExpandPermissionTreeRequest,
    ExpandPermissionTreeResponse,
    LookupResourcesRequest,
    LookupResourcesResponse,
    LookupSubjectsRequest,
    LookupSubjectsResponse,
    Precondition,
    ReadRelationshipsRequest,
    ReadRelationshipsResponse,
    RelationshipFilter,
    SubjectFilter,
    WriteRelationshipsRequest,
    WriteRelationshipsResponse,
)
from authzed.api.v1.permission_service_pb2_grpc import PermissionsServiceStub
from authzed.api.v1.schema_service_pb2 import (
    ReadSchemaRequest,
    ReadSchemaResponse,
    WriteSchemaRequest,
    WriteSchemaResponse,
)
from authzed.api.v1.schema_service_pb2_grpc import SchemaServiceStub
from authzed.api.v1.watch_service_pb2 import WatchRequest, WatchResponse
from authzed.api.v1.watch_service_pb2_grpc import WatchServiceStub


class Client(SchemaServiceStub, PermissionsServiceStub, ExperimentalServiceStub, WatchServiceStub):
    """
    v1 Authzed gRPC API client - Auto-detects sync or async depending on if initialized within an event loop
    """

    def __init__(self, target, credentials, options=None, compression=None):
        channel = self.create_channel(target, credentials, options, compression)
        self.init_stubs(channel)

    def init_stubs(self, channel):
        SchemaServiceStub.__init__(self, channel)
        PermissionsServiceStub.__init__(self, channel)
        ExperimentalServiceStub.__init__(self, channel)
        WatchServiceStub.__init__(self, channel)

    def create_channel(self, target, credentials, options=None, compression=None):
        try:
            asyncio.get_running_loop()
            channelfn = grpc.aio.secure_channel
        except RuntimeError:
            channelfn = grpc.secure_channel

        return channelfn(target, credentials, options, compression)


class AsyncClient(Client):
    """
    v1 Authzed gRPC API client, for use with asyncio.
    """

    def __init__(self, target, credentials, options=None, compression=None):
        channel = grpc.aio.secure_channel(target, credentials, options, compression)
        self.init_stubs(channel)


class SyncClient(Client):
    """
    v1 Authzed gRPC API client, running synchronously.
    """

    def __init__(self, target, credentials, options=None, compression=None):
        channel = grpc.secure_channel(target, credentials, options, compression)
        self.init_stubs(channel)


class TokenAuthorization(ClientInterceptor):
    def __init__(self, token: str):
        self._token = token

    def intercept(
        self,
        method: Callable,
        request_or_iterator: Any,
        call_details: grpc.ClientCallDetails,
    ):
        metadata: list[tuple[str, str | bytes]] = [("authorization", f"Bearer {self._token}")]
        if call_details.metadata is not None:
            metadata = [*metadata, *call_details.metadata]

        new_details = ClientCallDetails(
            call_details.method,
            call_details.timeout,
            metadata,
            call_details.credentials,
            call_details.wait_for_ready,
            call_details.compression,
        )

        return method(request_or_iterator, new_details)


class InsecureClient(Client):
    """
    An insecure client variant for non-TLS contexts.

    The default behavior of the python gRPC client is to restrict non-TLS
    calls to `localhost` only, which is frustrating in contexts like docker-compose,
    so we provide this as a convenience.
    """

    def __init__(
        self,
        target: str,
        token: str,
        options=None,
        compression=None,
    ):
        fake_credentials = grpc.local_channel_credentials()
        channel = self.create_channel(target, fake_credentials, options, compression)
        auth_interceptor = TokenAuthorization(token)

        insecure_channel = grpc.insecure_channel(target, options, compression)
        channel = grpc.intercept_channel(insecure_channel, auth_interceptor)

        self.init_stubs(channel)


__all__ = [
    "Client",
    # Core
    "AlgebraicSubjectSet",
    "ContextualizedCaveat",
    "DirectSubjectSet",
    "ObjectReference",
    "PermissionRelationshipTree",
    "Relationship",
    "RelationshipUpdate",
    "SubjectReference",
    "ZedToken",
    # Error Reason
    "ErrorReason",
    # Permission Service
    "CheckBulkPermissionsPair",
    "CheckBulkPermissionsRequest",
    "CheckBulkPermissionsRequestItem",
    "CheckBulkPermissionsResponse",
    "CheckBulkPermissionsResponseItem",
    "CheckPermissionRequest",
    "CheckPermissionResponse",
    "Consistency",
    "Cursor",
    "DeleteRelationshipsRequest",
    "DeleteRelationshipsResponse",
    "ExpandPermissionTreeRequest",
    "ExpandPermissionTreeResponse",
    "InsecureClient",
    "LookupResourcesRequest",
    "LookupResourcesResponse",
    "LookupSubjectsRequest",
    "LookupSubjectsResponse",
    "Precondition",
    "ReadRelationshipsRequest",
    "ReadRelationshipsResponse",
    "RelationshipFilter",
    "SubjectFilter",
    "WriteRelationshipsRequest",
    "WriteRelationshipsResponse",
    # Schema Service
    "ReadSchemaRequest",
    "ReadSchemaResponse",
    "WriteSchemaRequest",
    "WriteSchemaResponse",
    # Watch Service
    "WatchRequest",
    "WatchResponse",
    # Experimental Service
    "BulkCheckPermissionRequest",
    "BulkCheckPermissionResponse",
    "BulkCheckPermissionPair",
    "BulkCheckPermissionRequestItem",
    "BulkCheckPermissionResponseItem",
    "BulkImportRelationshipsRequest",
    "BulkImportRelationshipsResponse",
    "BulkExportRelationshipsRequest",
    "BulkExportRelationshipsResponse",
]
