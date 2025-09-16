import asyncio
import uuid
from unittest.mock import AsyncMock, MagicMock, Mock, patch

import grpc
import pytest
from google.protobuf.empty_pb2 import Empty

from authzed.api.v1 import (
    ConflictStrategy,
    ObjectReference,
    Relationship,
    RelationshipUpdate,
    RetryableClient,
    SubjectReference,
    WriteRelationshipsResponse,
)
from authzed.api.v1.experimental_service_pb2 import BulkImportRelationshipsResponse
from grpcutil import insecure_bearer_token_credentials
from inspect import isawaitable


async def maybe_await(resp):
    """Helper function to handle both sync and async responses."""
    if isawaitable(resp):
        resp = await resp
    return resp


# Create fixtures for mocked sync and async clients
@pytest.fixture()
def sync_retryable_client(token) -> RetryableClient:
    with patch.object(RetryableClient, 'create_channel') as mock_create_channel:
        mock_channel = Mock()
        mock_create_channel.return_value = mock_channel
        client = RetryableClient("localhost:50051", insecure_bearer_token_credentials(token))
        
        # Mock all the key methods we'll use in testing
        client.BulkImportRelationships = Mock()
        client.WriteRelationships = Mock(return_value=WriteRelationshipsResponse())
        
        return client


@pytest.fixture()
async def async_retryable_client(token) -> RetryableClient:
    with patch.object(RetryableClient, 'create_channel') as mock_create_channel:
        mock_channel = Mock()
        mock_create_channel.return_value = mock_channel
        client = RetryableClient("localhost:50051", insecure_bearer_token_credentials(token))
        
        # Mock all the key methods we'll use in testing
        client.BulkImportRelationships = AsyncMock()
        client.WriteRelationships = AsyncMock(return_value=WriteRelationshipsResponse())
        
        # Force async mode
        client._is_async = True
        
        return client


@pytest.fixture(params=["sync", "async"])
def retryable_client(
    request,
    sync_retryable_client: RetryableClient,
    async_retryable_client: RetryableClient,
):
    clients = {
        "sync": sync_retryable_client,
        "async": async_retryable_client,
    }
    return clients[request.param]


@pytest.fixture
def sample_relationships():
    """Return sample relationships for testing."""
    return [
        Relationship(
            resource=ObjectReference(object_type="document", object_id="doc1"),
            relation="viewer",
            subject=SubjectReference(
                object=ObjectReference(object_type="user", object_id="user1")
            ),
        ),
    ]


@patch("asyncio.iscoroutinefunction")
async def test_successful_bulk_import(mock_is_coro, retryable_client, sample_relationships):
    """Test that bulk import works without errors using mocks."""
    # Configure mocks
    mock_is_coro.return_value = isinstance(retryable_client.WriteRelationships, AsyncMock)
    
    # For both sync and async, simply return the response directly
    if isinstance(retryable_client.BulkImportRelationships, AsyncMock):
        retryable_client.BulkImportRelationships.return_value = BulkImportRelationshipsResponse()
    else:
        retryable_client.BulkImportRelationships.return_value = BulkImportRelationshipsResponse()
    
    # Import with TOUCH conflict strategy
    result = await maybe_await(
        retryable_client.retryable_bulk_import_relationships(
            relationships=sample_relationships,
            conflict_strategy=ConflictStrategy.TOUCH,
        )
    )
    
    # Verify the expected methods were called
    assert retryable_client.BulkImportRelationships.called
    
    # If we get here without errors, the test passes
    assert result is not None


@patch("authzed.api.v1.retryable_client.RetryableClient._is_already_exists_error")
@patch("asyncio.iscoroutinefunction")
async def test_skip_conflict_strategy(mock_is_coro, mock_already_exists, retryable_client, sample_relationships):
    """Test that SKIP strategy works as expected."""
    # Configure mock behaviors
    mock_already_exists.return_value = True
    mock_is_coro.return_value = isinstance(retryable_client.WriteRelationships, AsyncMock)
    
    # Set up the mock to raise an error when called
    error = grpc.RpcError("Already exists")
    if isinstance(retryable_client.BulkImportRelationships, AsyncMock):
        retryable_client.BulkImportRelationships.side_effect = error
    else:
        retryable_client.BulkImportRelationships.side_effect = error
    
    # Test import with SKIP conflict strategy
    result = await maybe_await(
        retryable_client.retryable_bulk_import_relationships(
            relationships=sample_relationships,
            conflict_strategy=ConflictStrategy.SKIP,
        )
    )
    
    # Should return None (indicating skipped)
    assert result is None


@patch("authzed.api.v1.retryable_client.RetryableClient._is_already_exists_error")
@patch("authzed.api.v1.retryable_client.RetryableClient._write_batches_with_retry_sync")
@patch("authzed.api.v1.retryable_client.RetryableClient._write_batches_with_retry_async")
@patch("asyncio.iscoroutinefunction")
async def test_touch_conflict_strategy(
    mock_is_coro,
    mock_write_async, 
    mock_write_sync, 
    mock_already_exists, 
    retryable_client,
    sample_relationships
):
    """Test that TOUCH strategy calls the correct retry method."""
    # Configure mock behaviors
    mock_already_exists.return_value = True
    mock_write_sync.return_value = WriteRelationshipsResponse()
    mock_write_async.return_value = WriteRelationshipsResponse()
    mock_is_coro.return_value = isinstance(retryable_client.WriteRelationships, AsyncMock)
    
    # Set up the mock to raise an error when called
    error = grpc.RpcError("Already exists")
    if isinstance(retryable_client.BulkImportRelationships, AsyncMock):
        retryable_client.BulkImportRelationships.side_effect = error
    else:
        retryable_client.BulkImportRelationships.side_effect = error
    
    # Test import with TOUCH conflict strategy
    await maybe_await(
        retryable_client.retryable_bulk_import_relationships(
            relationships=sample_relationships,
            conflict_strategy=ConflictStrategy.TOUCH,
        )
    )
    
    # Verify the correct retry method was called
    if isinstance(retryable_client.BulkImportRelationships, AsyncMock):
        assert mock_write_async.called
        assert not mock_write_sync.called
    else:
        assert not mock_write_async.called
        assert mock_write_sync.called


@patch("authzed.api.v1.retryable_client.RetryableClient._is_already_exists_error")
@patch("asyncio.iscoroutinefunction")
async def test_fail_conflict_strategy(mock_is_coro, mock_already_exists, retryable_client, sample_relationships):
    """Test that FAIL strategy raises an error when conflicts occur."""
    # Configure mock behaviors
    mock_already_exists.return_value = True
    mock_is_coro.return_value = isinstance(retryable_client.WriteRelationships, AsyncMock)
    
    # Set up the mock to raise an error when called
    error = grpc.RpcError("Already exists")
    if isinstance(retryable_client.BulkImportRelationships, AsyncMock):
        retryable_client.BulkImportRelationships.side_effect = error
    else:
        retryable_client.BulkImportRelationships.side_effect = error
    
    # Test import with FAIL conflict strategy
    with pytest.raises(ValueError, match="Duplicate relationships found"):
        await maybe_await(
            retryable_client.retryable_bulk_import_relationships(
                relationships=sample_relationships,
                conflict_strategy=ConflictStrategy.FAIL,
            )
        )


@patch("authzed.api.v1.retryable_client.RetryableClient._is_retryable_error")
@patch("time.sleep")
async def test_retry_with_backoff_sync(mock_sleep, mock_retryable, retryable_client, sample_relationships):
    """Test retrying with exponential backoff."""
    # Only run this test for sync client
    if isinstance(retryable_client.WriteRelationships, AsyncMock):
        pytest.skip("This test is for sync client only")
        
    # Setup for a retryable error that succeeds after 2 attempts
    mock_retryable.side_effect = [True, True, False]
    
    # Create a mock that raises errors for the first two calls, then succeeds
    mock_write = Mock()
    mock_write.side_effect = [
        grpc.RpcError("Retryable error"),
        grpc.RpcError("Retryable error"),
        WriteRelationshipsResponse(),
    ]
    
    # Apply the mock
    retryable_client.WriteRelationships = mock_write
    
    # Test the retry mechanism
    result = retryable_client._write_batches_with_retry_sync(sample_relationships, 30)
    
    # Verify the correct number of retries occurred
    assert mock_write.call_count == 3
    assert mock_sleep.call_count == 2
    
    # Verify backoff increased
    assert mock_sleep.call_args_list[0][0][0] < mock_sleep.call_args_list[1][0][0]


@patch("authzed.api.v1.retryable_client.RetryableClient._is_retryable_error")
@patch("asyncio.sleep")
async def test_retry_with_backoff_async(mock_sleep, mock_retryable, retryable_client, sample_relationships):
    """Test retrying with exponential backoff (async version)."""
    # Only run this test for async client
    if not isinstance(retryable_client.WriteRelationships, AsyncMock):
        pytest.skip("This test is for async client only")
        
    # Setup for a retryable error that succeeds after 2 attempts
    mock_retryable.side_effect = [True, True, False]
    
    # Create a mock that raises errors for the first two calls, then succeeds
    mock_write = AsyncMock()
    mock_write.side_effect = [
        grpc.RpcError("Retryable error"),
        grpc.RpcError("Retryable error"),
        WriteRelationshipsResponse(),
    ]
    
    # Apply the mock
    retryable_client.WriteRelationships = mock_write
    
    # Test the retry mechanism
    result = await retryable_client._write_batches_with_retry_async(sample_relationships, 30)
    
    # Verify the correct number of retries occurred
    assert mock_write.call_count == 3
    assert mock_sleep.call_count == 2
    
    # Verify backoff increased
    assert mock_sleep.call_args_list[0][0][0] < mock_sleep.call_args_list[1][0][0]


@patch("authzed.api.v1.retryable_client.RetryableClient._is_retryable_error")
async def test_max_retries_exceeded(mock_retryable, retryable_client, sample_relationships):
    """Test that retry count is limited."""
    # Always report retryable error
    mock_retryable.return_value = True
    
    # Create a mock that always raises errors
    if isinstance(retryable_client.WriteRelationships, AsyncMock):
        mock_write = AsyncMock(side_effect=grpc.RpcError("Always retryable error"))
        retryable_client.WriteRelationships = mock_write
        
        # Should eventually fail after max retries
        with pytest.raises(ValueError, match="Failed to write relationships after retry"):
            await retryable_client._write_batches_with_retry_async(sample_relationships, 30)
    else:
        mock_write = Mock(side_effect=grpc.RpcError("Always retryable error"))
        retryable_client.WriteRelationships = mock_write
        
        # Should eventually fail after max retries
        with pytest.raises(ValueError, match="Failed to write relationships after retry"):
            retryable_client._write_batches_with_retry_sync(sample_relationships, 30)
    
    # Verify retry count (DEFAULT_MAX_RETRIES + 1)
    assert mock_write.call_count == 11  # 10 retries + 1 initial attempt


def test_error_detection_methods():
    """Test the error classification methods."""
    client = RetryableClient("localhost:50051", insecure_bearer_token_credentials("token"))
    
    # Test _is_already_exists_error
    already_exists_error = grpc.RpcError()
    already_exists_error.code = lambda: grpc.StatusCode.ALREADY_EXISTS
    assert client._is_already_exists_error(already_exists_error) is True
    
    sql_error = Exception("SQLSTATE 23505 duplicate key value violates constraint")
    assert client._is_already_exists_error(sql_error) is True
    
    # Test _is_retryable_error
    unavailable_error = grpc.RpcError()
    unavailable_error.code = lambda: grpc.StatusCode.UNAVAILABLE
    assert client._is_retryable_error(unavailable_error) is True
    
    retry_error = Exception("retryable error: restart transaction")
    assert client._is_retryable_error(retry_error) is True
    
    # Test _is_canceled_error
    canceled_error = grpc.RpcError()
    canceled_error.code = lambda: grpc.StatusCode.CANCELLED
    assert client._is_canceled_error(canceled_error) is True
    
    timeout_error = asyncio.CancelledError()
    assert client._is_canceled_error(timeout_error) is True