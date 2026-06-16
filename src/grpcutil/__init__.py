from typing import Optional

import grpc


class AuthzedError(Exception):
    """Unified exception for both sync and async gRPC errors.

    This exception wraps both grpc.RpcError (sync) and grpc.aio.AioRpcError (async)
    to provide a consistent exception type for error handling.
    """

    def __init__(self, message: str, grpc_error: grpc.RpcError):
        super().__init__(message)
        self.grpc_error = grpc_error

    @classmethod
    def from_grpc_error(cls, error: grpc.RpcError) -> "AuthzedError":
        """Create an AuthzedError from a gRPC error."""
        return cls(str(error), error)


def bearer_token_credentials(token: str, certChain: Optional[bytes] = None):
    """
    gRPC credentials for a service that requires a Bearer Token.
    """
    return grpc.composite_channel_credentials(
        grpc.ssl_channel_credentials(root_certificates=certChain),
        grpc.access_token_call_credentials(token),
    )


def insecure_bearer_token_credentials(token: str):
    """
    gRPC credentials for an insecure service that requires a Bearer Token.

    This should only be used for testing.
    """
    return grpc.composite_channel_credentials(
        grpc.local_channel_credentials(grpc.LocalConnectionType.LOCAL_TCP),
        grpc.access_token_call_credentials(token),
    )
