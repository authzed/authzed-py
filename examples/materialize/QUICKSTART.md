# Materialize API Quick Start

The Materialize API allows you to build and maintain a materialized view of SpiceDB permissions in your own data store for high-performance lookups.

## Installation

```bash
# Install authzed with UV
uv add authzed

# Or with pip
pip install authzed
```

## Basic Usage

### 1. Initial Backfill with LookupPermissionSets

Use `LookupPermissionSets` to perform the initial backfill of permission sets:

```python
from authzed.api.materialize.v0 import (
    Client,
    LookupPermissionSetsRequest,
)
from grpcutil import bearer_token_credentials

# Create client
client = Client(
    "grpc.authzed.com:443",
    bearer_token_credentials("your_materialize_token"),
)

# Fetch permission sets
request = LookupPermissionSetsRequest(limit=1000)
response_stream = client.LookupPermissionSets(request)

for response in response_stream:
    change = response.change
    parent = change.parent_set

    # Store in your database
    print(f"Parent: {parent.object_type}:{parent.object_id}#{parent.permission_or_relation}")

    if change.HasField("child_member"):
        member = change.child_member
        print(f"  -> Member: {member.object_type}:{member.object_id}")
```

### 2. Watch for Updates with WatchPermissionSets

After backfilling, watch for ongoing changes:

```python
from authzed.api.materialize.v0 import (
    Client,
    WatchPermissionSetsRequest,
    PermissionSetChange,
)
from grpcutil import bearer_token_credentials

client = Client(
    "grpc.authzed.com:443",
    bearer_token_credentials("your_materialize_token"),
)

request = WatchPermissionSetsRequest(
    optional_starting_after=last_revision,  # From your last LookupPermissionSets backfill
)

response_stream = client.WatchPermissionSets(request)

for response in response_stream:
    change = response.change

    # Handle the operation type
    if change.operation == PermissionSetChange.SET_OPERATION_ADDED:
        # Add to materialized view
        pass
    elif change.operation == PermissionSetChange.SET_OPERATION_REMOVED:
        # Remove from materialized view
        pass
```

### 3. Local Development

For local Materialize instances without TLS:

```python
from authzed.api.materialize.v0 import (
    InsecureClient,
    LookupPermissionSetsRequest,
)

client = InsecureClient("localhost:50051", "your_local_token")

request = LookupPermissionSetsRequest(limit=100)
response_stream = client.LookupPermissionSets(request)

for response in response_stream:
    # Process responses
    pass
```

### 4. Async Usage

```python
import asyncio
from authzed.api.materialize.v0 import (
    AsyncClient,
    LookupPermissionSetsRequest,
)
from grpcutil import bearer_token_credentials

async def fetch_permission_sets():
    client = AsyncClient(
        "grpc.authzed.com:443",
        bearer_token_credentials("your_materialize_token"),
    )
    request = LookupPermissionSetsRequest(limit=1000)

    response_stream = client.LookupPermissionSets(request)

    async for response in response_stream:
        # Process responses asynchronously
        pass

asyncio.run(fetch_permission_sets())
```

## Pagination

### Synchronous Pagination

Handle large datasets with cursor-based pagination:

```python
from authzed.api.materialize.v0 import (
    Client,
    LookupPermissionSetsRequest,
)
from grpcutil import bearer_token_credentials

client = Client(
    "grpc.authzed.com:443",
    bearer_token_credentials("your_materialize_token"),
)

cursor = None
total_processed = 0

while True:
    request = LookupPermissionSetsRequest(
        limit=1000,
        optional_starting_after_cursor=cursor,
    )

    count = 0
    for response in client.LookupPermissionSets(request):
        # Process response
        change = response.change
        parent = change.parent_set
        print(f"Processed: {parent.object_type}:{parent.object_id}#{parent.permission_or_relation}")

        count += 1
        total_processed += 1
        cursor = response.cursor if response.HasField("cursor") else None

    print(f"Batch complete: {count} permission sets (total: {total_processed})")

    # If we got fewer results than limit, we're done
    if count < 1000:
        break

print(f"Pagination complete! Total: {total_processed}")
```

### Async Pagination

For async/await usage with automatic pagination:

```python
import asyncio
import grpc
from authzed.api.materialize.v0 import (
    AsyncClient,
    LookupPermissionSetsRequest,
)
from grpcutil import bearer_token_credentials

async def paginate_permission_sets():
    client = AsyncClient(
        "grpc.authzed.com:443",
        bearer_token_credentials("your_materialize_token"),
    )

    cursor = None
    total_processed = 0
    batch_size = 1000

    while True:
        request = LookupPermissionSetsRequest(
            limit=batch_size,
            optional_starting_after_cursor=cursor,
        )

        count = 0

        try:
            response_stream = client.LookupPermissionSets(request)

            async for response in response_stream:
                # Process response
                change = response.change
                parent = change.parent_set
                print(f"Processed: {parent.object_type}:{parent.object_id}#{parent.permission_or_relation}")

                count += 1
                total_processed += 1

                # Update cursor for next batch
                if response.HasField("cursor"):
                    cursor = response.cursor

            print(f"Batch complete: {count} permission sets (total: {total_processed})")

            # If we got fewer results than limit, we're done
            if count < batch_size:
                break

        except grpc.aio.AioRpcError as e:
            print(f"Error: {e.code()}: {e.details()}")
            break

    print(f"Pagination complete! Total: {total_processed}")

# Run the async function
asyncio.run(paginate_permission_sets())
```

## Client Types

### Overview

The package provides multiple client types for different use cases:

| Client | Sync/Async | Detection | Best For |
|--------|-----------|-----------|----------|
| `Client` | Both | Auto-detect | General use, adapts to context |
| `SyncClient` | Sync only | Explicit | Synchronous code, better type hints |
| `AsyncClient` | Async only | Explicit | Async code with asyncio, better type hints |
| `InsecureClient` | Both | Auto-detect | Local dev without TLS |

## Resources

- [Materialize Documentation](https://authzed.com/docs/authzed/concepts/authzed-materialize)
- [Materialize API Reference](https://buf.build/authzed/api/docs/main:authzed.api.materialize.v0)
