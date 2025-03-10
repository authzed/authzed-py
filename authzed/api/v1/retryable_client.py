import asyncio
import enum
import time
from typing import List, Optional

import grpc
from google.rpc import code_pb2
from grpc import StatusCode

from authzed.api.v1 import Client, Relationship, RelationshipUpdate
from authzed.api.v1.experimental_service_pb2 import BulkImportRelationshipsRequest
from authzed.api.v1.permission_service_pb2 import WriteRelationshipsRequest

# Default configuration
DEFAULT_BACKOFF_MS = 50
DEFAULT_MAX_RETRIES = 10
DEFAULT_MAX_BACKOFF_MS = 2000
DEFAULT_TIMEOUT_SECONDS = 30


class ConflictStrategy(enum.Enum):
    """Strategy to handle conflicts during bulk relationship import."""
    FAIL = 0  # The operation will fail if any duplicate relationships are found
    SKIP = 1  # The operation will ignore duplicates and continue with the import
    TOUCH = 2  # The operation will retry with TOUCH semantics for duplicates


# Datastore error strings for older versions of SpiceDB
TX_CONFLICT_STRINGS = [
    "SQLSTATE 23505",      # CockroachDB
    "Error 1062 (23000)",  # MySQL
]

RETRYABLE_ERROR_STRINGS = [
    "retryable error",                          # CockroachDB, PostgreSQL
    "try restarting transaction", "Error 1205", # MySQL
]


class RetryableClient(Client):
    """
    A client for SpiceDB that adds retryable operations with support for
    different conflict strategies. This client extends the base Client with
    additional functionality for handling transaction conflicts.
    """

    def __init__(self, target, credentials, options=None, compression=None):
        super().__init__(target, credentials, options, compression)

    def retryable_bulk_import_relationships(
        self,
        relationships: List[Relationship],
        conflict_strategy: ConflictStrategy,
        timeout_seconds: Optional[int] = None
    ):
        """
        Import relationships with configurable retry behavior based on conflict strategy.
        
        Args:
            relationships: List of relationships to import
            conflict_strategy: Strategy to use when conflicts are detected
            timeout_seconds: Optional timeout in seconds for the operation
            
        Returns:
            The response from the successful import operation
            
        Raises:
            Exception: If the import fails and cannot be retried
        """
        if asyncio.iscoroutinefunction(self.BulkImportRelationships):
            return self._retryable_bulk_import_relationships_async(
                relationships, conflict_strategy, timeout_seconds
            )
        else:
            return self._retryable_bulk_import_relationships_sync(
                relationships, conflict_strategy, timeout_seconds
            )

    def _retryable_bulk_import_relationships_sync(
        self,
        relationships: List[Relationship],
        conflict_strategy: ConflictStrategy,
        timeout_seconds: Optional[int] = None
    ):
        """Synchronous implementation of retryable bulk import."""
        timeout = timeout_seconds or DEFAULT_TIMEOUT_SECONDS
        
        # Create a generator function to yield requests
        def request_iterator():
            yield BulkImportRelationshipsRequest(relationships=relationships)
        
        # Try bulk import first - correctly passing the request iterator
        try:
            response = self.BulkImportRelationships(request_iterator(), timeout=timeout)
            return response  # Success on first try
        except Exception as err:
            # Handle errors based on type and conflict strategy
            if self._is_canceled_error(err):
                raise err
                
            if self._is_already_exists_error(err) and conflict_strategy == ConflictStrategy.SKIP:
                return None  # Skip conflicts
                
            if self._is_retryable_error(err) or (
                self._is_already_exists_error(err) and 
                conflict_strategy == ConflictStrategy.TOUCH
            ):
                # Retry with write_relationships_with_retry
                return self._write_batches_with_retry_sync(relationships, timeout)
                
            if self._is_already_exists_error(err) and conflict_strategy == ConflictStrategy.FAIL:
                raise ValueError("Duplicate relationships found")
                
            # Default case - propagate the error
            raise ValueError(f"Error finalizing write of {len(relationships)} relationships: {err}")

    async def _retryable_bulk_import_relationships_async(
        self,
        relationships: List[Relationship],
        conflict_strategy: ConflictStrategy,
        timeout_seconds: Optional[int] = None
    ):
        """Asynchronous implementation of retryable bulk import."""
        timeout = timeout_seconds or DEFAULT_TIMEOUT_SECONDS
        
        # Create an async generator function to yield requests
        async def request_iterator():
            yield BulkImportRelationshipsRequest(relationships=relationships)
        
        # Try bulk import first - correctly passing the request iterator
        try:
            response = await self.BulkImportRelationships(request_iterator(), timeout=timeout)
            return response  # Success on first try
        except Exception as err:
            # Handle errors based on type and conflict strategy
            if self._is_canceled_error(err):
                raise err
                
            if self._is_already_exists_error(err) and conflict_strategy == ConflictStrategy.SKIP:
                return None  # Skip conflicts
                
            if self._is_retryable_error(err) or (
                self._is_already_exists_error(err) and 
                conflict_strategy == ConflictStrategy.TOUCH
            ):
                # Retry with write_relationships_with_retry
                return await self._write_batches_with_retry_async(relationships, timeout)
                
            if self._is_already_exists_error(err) and conflict_strategy == ConflictStrategy.FAIL:
                raise ValueError("Duplicate relationships found")
                
            # Default case - propagate the error
            raise ValueError(f"Error finalizing write of {len(relationships)} relationships: {err}")

    def _write_batches_with_retry_sync(self, relationships: List[Relationship], timeout_seconds: int):
        """
        Retry writing relationships in batches with exponential backoff.
        This is a synchronous implementation.
        """
        updates = [
            RelationshipUpdate(
                relationship=rel,
                operation=RelationshipUpdate.OPERATION_TOUCH
            )
            for rel in relationships
        ]
        
        backoff_ms = DEFAULT_BACKOFF_MS
        current_retries = 0
        
        while True:
            try:
                request = WriteRelationshipsRequest(updates=updates)
                response = self.WriteRelationships(request, timeout=timeout_seconds)
                return response
            except Exception as err:
                if self._is_retryable_error(err) and current_retries < DEFAULT_MAX_RETRIES:
                    # Throttle writes with exponential backoff
                    time.sleep(backoff_ms / 1000)
                    backoff_ms = min(backoff_ms * 2, DEFAULT_MAX_BACKOFF_MS)
                    current_retries += 1
                    continue
                
                # Non-retryable error or max retries exceeded
                raise ValueError(f"Failed to write relationships after retry: {err}")

    async def _write_batches_with_retry_async(self, relationships: List[Relationship], timeout_seconds: int):
        """
        Retry writing relationships in batches with exponential backoff.
        This is an asynchronous implementation.
        """
        updates = [
            RelationshipUpdate(
                relationship=rel,
                operation=RelationshipUpdate.OPERATION_TOUCH
            )
            for rel in relationships
        ]
        
        backoff_ms = DEFAULT_BACKOFF_MS
        current_retries = 0
        
        while True:
            try:
                request = WriteRelationshipsRequest(updates=updates)
                response = await self.WriteRelationships(request, timeout=timeout_seconds)
                return response
            except Exception as err:
                if self._is_retryable_error(err) and current_retries < DEFAULT_MAX_RETRIES:
                    # Throttle writes with exponential backoff
                    await asyncio.sleep(backoff_ms / 1000)
                    backoff_ms = min(backoff_ms * 2, DEFAULT_MAX_BACKOFF_MS)
                    current_retries += 1
                    continue
                
                # Non-retryable error or max retries exceeded
                raise ValueError(f"Failed to write relationships after retry: {err}")

    def _is_already_exists_error(self, err):
        """Check if the error is an 'already exists' error."""
        if err is None:
            return False
            
        if self._is_grpc_code(err, StatusCode.ALREADY_EXISTS):
            return True
            
        return self._contains_error_string(err, TX_CONFLICT_STRINGS)

    def _is_retryable_error(self, err):
        """Check if the error is retryable."""
        if err is None:
            return False
            
        if self._is_grpc_code(err, StatusCode.UNAVAILABLE, StatusCode.DEADLINE_EXCEEDED):
            return True
            
        if self._contains_error_string(err, RETRYABLE_ERROR_STRINGS):
            return True
            
        return isinstance(err, asyncio.TimeoutError) or isinstance(getattr(err, "__cause__", None), asyncio.TimeoutError)

    def _is_canceled_error(self, err):
        """Check if the error is a cancellation error."""
        if err is None:
            return False
            
        if isinstance(err, asyncio.CancelledError):
            return True
            
        if self._is_grpc_code(err, StatusCode.CANCELLED):
            return True
            
        return False

    def _contains_error_string(self, err, error_strings):
        """Check if the error message contains any of the given strings."""
        if err is None:
            return False
            
        err_str = str(err)
        return any(es in err_str for es in error_strings)

    def _is_grpc_code(self, err, *codes):
        """Check if the error is a gRPC error with one of the given status codes."""
        if err is None:
            return False
            
        try:
            status = grpc.StatusCode(err.code())
            return status in codes
        except (ValueError, AttributeError):
            # If we can't extract a gRPC status code, it's not a gRPC error
            return False