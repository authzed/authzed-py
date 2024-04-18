from authzed.api.v1.schema_service_pb2_grpc import SchemaServiceStub, SchemaServiceAsyncStub
from authzed.api.v1.experimental_service_pb2_grpc import (
    ExperimentalServiceStub,
    ExperimentalServiceAsyncStub,
)
from authzed.api.v1.permission_service_pb2_grpc import (
    PermissionsServiceStub,
    PermissionsServiceAsyncStub,
)
from authzed.api.v1.watch_service_pb2_grpc import WatchServiceStub, WatchServiceAsyncStub
import grpc
from typing import Optional, Sequence, Tuple, Any

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
