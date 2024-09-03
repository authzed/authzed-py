import pytest
import grpc

from authzed.api.v1 import (
        InsecureClient,
        SyncClient,
        AsyncClient,
        )
from grpcutil import insecure_bearer_token_credentials

from .calls import write_test_schema

# NOTE: this is the name of the "remote" binding of the service container
# in CI. These tests are only run in CI because otherwise setup is fiddly.
# If you want to see these tests run locally, figure out your computer's
# network-local IP address (typically 192.168.x.x) and make that the `remote_host`
# string below, and then start up a testing container bound to that interface:
# docker run --rm -p 192.168.x.x:50051:50051 authzed/spicedb serve-testing
remote_host = "remote-spicedb"

@pytest.mark.ci_only
async def test_normal_async_client_raises_error_on_insecure_remote_call(token):
    with pytest.raises(grpc.RpcError):
        client = AsyncClient(f"{remote_host}:50051", insecure_bearer_token_credentials(token))
        await write_test_schema(client)

@pytest.mark.ci_only
async def test_normal_sync_client_raises_error_on_insecure_remote_call(token):
    with pytest.raises(grpc.RpcError):
        client = SyncClient(f"{remote_host}:50051", insecure_bearer_token_credentials(token))
        await write_test_schema(client)

@pytest.mark.ci_only
async def test_insecure_client_makes_insecure_remote_call(token):
    insecure_client = InsecureClient(f"{remote_host}:50051", token)
    await write_test_schema(insecure_client)
