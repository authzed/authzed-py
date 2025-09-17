from typing import Any, Optional, Sequence, Tuple

import grpc

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
from authzed.api.v1.experimental_service_pb2_grpc import (
    ExperimentalServiceAsyncStub,
    ExperimentalServiceStub,
)
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
from authzed.api.v1.permission_service_pb2_grpc import (
    PermissionsServiceAsyncStub,
    PermissionsServiceStub,
)
from authzed.api.v1.schema_service_pb2 import (
    ReadSchemaRequest,
    ReadSchemaResponse,
    WriteSchemaRequest,
    WriteSchemaResponse,
)
from authzed.api.v1.schema_service_pb2_grpc import SchemaServiceAsyncStub, SchemaServiceStub
from authzed.api.v1.watch_service_pb2 import WatchRequest, WatchResponse
from authzed.api.v1.watch_service_pb2_grpc import WatchServiceAsyncStub, WatchServiceStub

class Client(SchemaServiceStub, PermissionsServiceStub, ExperimentalServiceStub, WatchServiceStub):
    """The Client is typed as a synchronous client (though in practice it works with both sync and async code).
    If you are using the async code, you should switch to the AsyncClient class instead in order to get proper type hints
    """

    def __init__(
        self,
        target: str,
        credentials: grpc.ChannelCredentials,
        options: Optional[Sequence[Tuple[str, Any]]] = None,
        compression: Optional[grpc.Compression] = None,
    ) -> None: ...

class SyncClient(
    SchemaServiceStub, PermissionsServiceStub, ExperimentalServiceStub, WatchServiceStub
):
    def __init__(
        self,
        target: str,
        credentials: grpc.ChannelCredentials,
        options: Optional[Sequence[Tuple[str, Any]]] = None,
        compression: Optional[grpc.Compression] = None,
    ) -> None: ...

class AsyncClient(
    SchemaServiceAsyncStub,
    PermissionsServiceAsyncStub,
    ExperimentalServiceAsyncStub,
    WatchServiceAsyncStub,
):
    def __init__(
        self,
        target: str,
        credentials: grpc.ChannelCredentials,
        options: Optional[Sequence[Tuple[str, Any]]] = None,
        compression: Optional[grpc.Compression] = None,
    ) -> None: ...

class InsecureClient(Client):
    def __init__(
        self,
        target: str,
        token: str,
        options=None,
        compression=None,
    ) -> None: ...

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
