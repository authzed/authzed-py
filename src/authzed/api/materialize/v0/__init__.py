import asyncio
from typing import Any, Callable

import grpc
import grpc.aio
from grpc_interceptor import ClientCallDetails, ClientInterceptor

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
    """
    v0 Materialize gRPC API client - Auto-detects sync or async depending on if initialized within an event loop
    """

    def __init__(self, target, credentials, options=None, compression=None):
        channel = self.create_channel(target, credentials, options, compression)
        self.init_stubs(channel)

    def init_stubs(self, channel):
        WatchPermissionsServiceStub.__init__(self, channel)
        WatchPermissionSetsServiceStub.__init__(self, channel)

    def create_channel(self, target, credentials, options=None, compression=None):
        try:
            asyncio.get_running_loop()
            channelfn = grpc.aio.secure_channel
        except RuntimeError:
            channelfn = grpc.secure_channel

        return channelfn(target, credentials, options, compression)


class AsyncClient(Client):
    """
    v0 Materialize gRPC API client, for use with asyncio.
    """

    def __init__(self, target, credentials, options=None, compression=None):
        channel = grpc.aio.secure_channel(target, credentials, options, compression)
        self.init_stubs(channel)


class SyncClient(Client):
    """
    v0 Materialize gRPC API client, running synchronously.
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
    # Clients
    "Client",
    "AsyncClient",
    "SyncClient",
    "InsecureClient",
    # Watch Permissions
    "PermissionChange",
    "WatchedPermission",
    "WatchPermissionsRequest",
    "WatchPermissionsResponse",
    "WatchPermissionsServiceStub",
    # Watch Permission Sets
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
