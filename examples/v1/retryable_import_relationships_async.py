#!/usr/bin/env python3

import asyncio
import os
import sys
from typing import List

import grpc
import grpc.aio

from authzed.api.v1 import (
    ConflictStrategy,
    ObjectReference,
    Relationship,
    RetryableClient,
    SubjectReference,
)

# Environment variables for configuration
AUTHZED_ENDPOINT = os.getenv("AUTHZED_ENDPOINT", "grpc.authzed.com:443")
AUTHZED_TOKEN = os.getenv("AUTHZED_TOKEN", "")


def create_sample_relationships() -> List[Relationship]:
    """Create a list of sample relationships for import."""
    relationships = []
    
    # Create 5 documents, each with view permissions for 2 users
    for i in range(5):
        doc_id = f"doc{i}"
        for j in range(2):
            user_id = f"user{j}"
            
            # Create a relationship where user can view document
            rel = Relationship(
                resource=ObjectReference(
                    object_type="document",
                    object_id=doc_id,
                ),
                relation="viewer",
                subject=SubjectReference(
                    object=ObjectReference(
                        object_type="user",
                        object_id=user_id,
                    ),
                ),
            )
            relationships.append(rel)
    
    return relationships


async def main():
    """
    Demonstrate usage of the RetryableClient for importing relationships
    with different conflict strategies using async/await.
    """
    if not AUTHZED_TOKEN:
        print("Error: AUTHZED_TOKEN environment variable is required")
        sys.exit(1)
    
    # Create channel credentials
    channel_creds = grpc.ssl_channel_credentials()
    
    # Create RetryableClient
    client = RetryableClient(
        AUTHZED_ENDPOINT,
        grpc.composite_channel_credentials(
            channel_creds,
            grpc.access_token_call_credentials(AUTHZED_TOKEN),
        ),
    )
    
    # Create sample relationships
    relationships = create_sample_relationships()
    print(f"Created {len(relationships)} sample relationships")
    
    # Import relationships with TOUCH conflict strategy
    print("Importing relationships with TOUCH conflict strategy...")
    try:
        await client.retryable_bulk_import_relationships(
            relationships=relationships,
            conflict_strategy=ConflictStrategy.TOUCH,
        )
        print("Import successful!")
    except Exception as e:
        print(f"Import failed: {e}")
    
    # Try to import the same relationships again, but with SKIP strategy
    print("\nImporting the same relationships again with SKIP conflict strategy...")
    try:
        await client.retryable_bulk_import_relationships(
            relationships=relationships,
            conflict_strategy=ConflictStrategy.SKIP,
        )
        print("Import successful (skipped duplicates)!")
    except Exception as e:
        print(f"Import failed: {e}")
    
    # Try to import the same relationships again, but with FAIL strategy
    print("\nImporting the same relationships again with FAIL conflict strategy...")
    try:
        await client.retryable_bulk_import_relationships(
            relationships=relationships,
            conflict_strategy=ConflictStrategy.FAIL,
        )
        print("Import successful!")
    except Exception as e:
        print(f"Import failed as expected: {e}")


if __name__ == "__main__":
    asyncio.run(main())