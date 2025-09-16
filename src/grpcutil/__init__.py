from typing import Optional

import grpc


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
