import asyncio

import grpc
import grpc.aio

from authzed.api.v0.acl_service_pb2 import (
    CheckRequest,
    CheckResponse,
    ContentChangeCheckRequest,
    ExpandRequest,
    ExpandResponse,
    LookupRequest,
    LookupResponse,
    ReadRequest,
    ReadResponse,
    RelationTupleFilter,
    WriteRequest,
    WriteResponse,
)
from authzed.api.v0.acl_service_pb2_grpc import ACLServiceStub
from authzed.api.v0.core_pb2 import (
    DirectUserset,
    ObjectAndRelation,
    RelationReference,
    RelationTuple,
    RelationTupleTreeNode,
    SetOperationUserset,
    User,
    Zookie,
)
from authzed.api.v0.developer_pb2_grpc import DeveloperServiceStub
from authzed.api.v0.namespace_pb2 import (
    ComputedUserset,
    Metadata,
    NamespaceDefinition,
    Relation,
    SetOperation,
    TupleToUserset,
    TypeInformation,
    UsersetRewrite,
)
from authzed.api.v0.namespace_service_pb2 import (
    ReadConfigRequest,
    ReadConfigResponse,
    WriteConfigRequest,
    WriteConfigResponse,
)
from authzed.api.v0.namespace_service_pb2_grpc import NamespaceServiceStub
from authzed.api.v0.watch_service_pb2_grpc import WatchServiceStub


class Client(ACLServiceStub, DeveloperServiceStub, NamespaceServiceStub, WatchServiceStub):
    """
    v0 Authzed gRPC API client.
    """

    def __init__(self, target, credentials, options=None, compression=None):
        channelfn = (
            grpc.aio.secure_channel
            if asyncio.get_event_loop().is_running()
            else grpc.secure_channel
        )
        channel = channelfn(target, credentials, options, compression)
        ACLServiceStub.__init__(self, channel)
        DeveloperServiceStub.__init__(self, channel)
        NamespaceServiceStub.__init__(self, channel)
        WatchServiceStub.__init__(self, channel)


__all__ = [
    "Client",
    # Core
    "DirectUserset",
    "ObjectAndRelation",
    "RelationReference",
    "RelationTuple",
    "RelationTupleTreeNode",
    "SetOperationUserset",
    "User",
    "Zookie",
    # Namespace
    "ComputedUserset",
    "Metadata",
    "NamespaceDefinition",
    "Relation",
    "SetOperation",
    "TupleToUserset",
    "TypeInformation",
    "UsersetRewrite",
    # ACL Service
    "CheckRequest",
    "CheckResponse",
    "ContentChangeCheckRequest",
    "ExpandRequest",
    "ExpandResponse",
    "LookupRequest",
    "LookupResponse",
    "ReadRequest",
    "ReadResponse",
    "RelationTupleFilter",
    "WriteRequest",
    "WriteResponse",
    # Namespace Service
    "ReadConfigRequest",
    "ReadConfigResponse",
    "WriteConfigRequest",
    "WriteConfigResponse",
]
