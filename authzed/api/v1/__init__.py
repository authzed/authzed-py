import asyncio

import grpc
import grpc.aio

from authzed.api.v1.core_pb2 import (
    AlgebraicSubjectSet,
    ContextualizedCaveat,
    DirectSubjectSet,
    ObjectReference,
    PermissionRelationshipTree,
    Relationship,
    RelationshipUpdate,
    SubjectReference,
    ZedToken,
)
from authzed.api.v1.error_reason_pb2 import ErrorReason
from authzed.api.v1.permission_service_pb2 import (
    CheckPermissionRequest,
    CheckPermissionResponse,
    Consistency,
    DeleteRelationshipsRequest,
    DeleteRelationshipsResponse,
    ExpandPermissionTreeRequest,
    ExpandPermissionTreeResponse,
    LookupResourcesRequest,
    LookupResourcesResponse,
    LookupSubjectsRequest,
    LookupSubjectsResponse,
    Precondition,
    ReadRelationshipsRequest,
    ReadRelationshipsResponse,
    RelationshipFilter,
    SubjectFilter,
    WriteRelationshipsRequest,
    WriteRelationshipsResponse,
)
from authzed.api.v1.permission_service_pb2_grpc import PermissionsServiceStub
from authzed.api.v1.schema_service_pb2 import (
    ReadSchemaRequest,
    ReadSchemaResponse,
    WriteSchemaRequest,
    WriteSchemaResponse,
)
from authzed.api.v1.schema_service_pb2_grpc import SchemaServiceStub


class Client(SchemaServiceStub, PermissionsServiceStub):
    """
    v1 Authzed gRPC API client.
    """

    def __init__(self, target, credentials, options=None, compression=None):
        try:
            asyncio.get_running_loop()
            channelfn = grpc.aio.secure_channel
        except RuntimeError:
            channelfn = grpc.secure_channel

        channel = channelfn(target, credentials, options, compression)
        SchemaServiceStub.__init__(self, channel)
        PermissionsServiceStub.__init__(self, channel)


__all__ = [
    "Client",
    # Core
    "AlgebraicSubjectSet",
    "ContextualizedCaveat",
    "DirectSubjectSet",
    "ObjectReference",
    "PermissionRelationshipTree",
    "Relationship",
    "RelationshipUpdate",
    "SubjectReference",
    "ZedToken",
    # Error Reason
    "ErrorReason",
    # Permission Service
    "CheckPermissionRequest",
    "CheckPermissionResponse",
    "Consistency",
    "DeleteRelationshipsRequest",
    "DeleteRelationshipsResponse",
    "ExpandPermissionTreeRequest",
    "ExpandPermissionTreeResponse",
    "LookupResourcesRequest",
    "LookupResourcesResponse",
    "LookupSubjectsRequest",
    "LookupSubjectsResponse",
    "Precondition",
    "ReadRelationshipsRequest",
    "ReadRelationshipsResponse",
    "RelationshipFilter",
    "SubjectFilter",
    "WriteRelationshipsRequest",
    "WriteRelationshipsResponse",
    # Schema Service
    "ReadSchemaRequest",
    "ReadSchemaResponse",
    "WriteSchemaRequest",
    "WriteSchemaResponse",
]
