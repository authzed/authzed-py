import asyncio

import grpc
import grpc.aio
import pytest

from authzed.api.v1 import AsyncClient, Client, InsecureClient, SyncClient
from grpcutil import insecure_bearer_token_credentials


def test_sync_client_close_closes_channel(token):
    client = SyncClient("localhost:50051", insecure_bearer_token_credentials(token))
    assert isinstance(client._channel, grpc.Channel)

    # close should be idempotent and not raise
    client.close()
    client.close()


def test_insecure_client_close_closes_channel(token):
    client = InsecureClient("localhost:50051", token)
    # InsecureClient uses an intercepted channel, but it still exposes close()
    client.close()
    client.close()


async def test_async_client_close_closes_channel(token):
    client = AsyncClient("localhost:50051", insecure_bearer_token_credentials(token))
    assert isinstance(client._channel, grpc.aio.Channel)

    # close should be awaitable and idempotent
    await client.close()
    await client.close()


async def test_async_client_close_accepts_grace(token):
    client = AsyncClient("localhost:50051", insecure_bearer_token_credentials(token))
    await client.close(grace=0)


def test_autodetect_client_close_when_sync(token):
    # Outside of an event loop, Client builds a sync channel; close() should
    # return None (not a coroutine).
    with pytest.raises(RuntimeError):
        asyncio.get_running_loop()
    client = Client("localhost:50051", insecure_bearer_token_credentials(token))
    assert isinstance(client._channel, grpc.Channel)
    result = client.close()
    assert result is None


async def test_autodetect_client_close_when_async(token):
    # Inside an event loop, Client builds an async channel; close() returns a
    # coroutine that must be awaited.
    client = Client("localhost:50051", insecure_bearer_token_credentials(token))
    assert isinstance(client._channel, grpc.aio.Channel)
    awaitable = client.close()
    assert asyncio.iscoroutine(awaitable)
    await awaitable
