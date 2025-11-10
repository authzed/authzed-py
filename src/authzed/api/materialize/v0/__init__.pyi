from typing import Any, Optional, Sequence, Tuple

import grpc

from authzed.api.materialize.v0.watchpermissions_pb2 import (
    PermissionChange,
    WatchedPermission,
    WatchPermissionsRequest,
    WatchPermissionsResponse,
)
from authzed.api.materialize.v0.watchpermissions_pb2_grpc import (
    WatchPermissionsServiceStub,
)
from authzed.api.materialize.v0.watchpermissionsets_pb2 import (
    BreakingSchemaChange,
    Cursor,
    DownloadPermissionSetsRequest,
    DownloadPermissionSetsResponse,
    File,
    LookupPermissionSetsRequest,
    LookupPermissionSetsRequired,
    LookupPermissionSetsResponse,
    MemberReference,
    PermissionSetChange,
    SetReference,
    WatchPermissionSetsRequest,
    WatchPermissionSetsResponse,
)
from authzed.api.materialize.v0.watchpermissionsets_pb2_grpc import (
    WatchPermissionSetsServiceStub,
)

class Client(WatchPermissionsServiceStub, WatchPermissionSetsServiceStub):
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

class SyncClient(WatchPermissionsServiceStub, WatchPermissionSetsServiceStub):
    def __init__(
        self,
        target: str,
        credentials: grpc.ChannelCredentials,
        options: Optional[Sequence[Tuple[str, Any]]] = None,
        compression: Optional[grpc.Compression] = None,
    ) -> None: ...

class AsyncClient(WatchPermissionsServiceStub, WatchPermissionSetsServiceStub):
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
    "AsyncClient",
    "SyncClient",
    "InsecureClient",
    "PermissionChange",
    "WatchedPermission",
    "WatchPermissionsRequest",
    "WatchPermissionsResponse",
    "WatchPermissionsServiceStub",
    "BreakingSchemaChange",
    "Cursor",
    "DownloadPermissionSetsRequest",
    "DownloadPermissionSetsResponse",
    "File",
    "LookupPermissionSetsRequest",
    "LookupPermissionSetsRequired",
    "LookupPermissionSetsResponse",
    "MemberReference",
    "PermissionSetChange",
    "SetReference",
    "WatchPermissionSetsRequest",
    "WatchPermissionSetsResponse",
    "WatchPermissionSetsServiceStub",
]
