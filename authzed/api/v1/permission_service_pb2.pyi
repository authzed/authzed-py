from google.protobuf import struct_pb2 as _struct_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.rpc import status_pb2 as _status_pb2
from validate import validate_pb2 as _validate_pb2
from authzed.api.v1 import core_pb2 as _core_pb2
from authzed.api.v1 import debug_pb2 as _debug_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LookupPermissionship(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LOOKUP_PERMISSIONSHIP_UNSPECIFIED: _ClassVar[LookupPermissionship]
    LOOKUP_PERMISSIONSHIP_HAS_PERMISSION: _ClassVar[LookupPermissionship]
    LOOKUP_PERMISSIONSHIP_CONDITIONAL_PERMISSION: _ClassVar[LookupPermissionship]
LOOKUP_PERMISSIONSHIP_UNSPECIFIED: LookupPermissionship
LOOKUP_PERMISSIONSHIP_HAS_PERMISSION: LookupPermissionship
LOOKUP_PERMISSIONSHIP_CONDITIONAL_PERMISSION: LookupPermissionship

class Consistency(_message.Message):
    __slots__ = ("minimize_latency", "at_least_as_fresh", "at_exact_snapshot", "fully_consistent")
    MINIMIZE_LATENCY_FIELD_NUMBER: _ClassVar[int]
    AT_LEAST_AS_FRESH_FIELD_NUMBER: _ClassVar[int]
    AT_EXACT_SNAPSHOT_FIELD_NUMBER: _ClassVar[int]
    FULLY_CONSISTENT_FIELD_NUMBER: _ClassVar[int]
    minimize_latency: bool
    at_least_as_fresh: _core_pb2.ZedToken
    at_exact_snapshot: _core_pb2.ZedToken
    fully_consistent: bool
    def __init__(self, minimize_latency: bool = ..., at_least_as_fresh: _Optional[_Union[_core_pb2.ZedToken, _Mapping]] = ..., at_exact_snapshot: _Optional[_Union[_core_pb2.ZedToken, _Mapping]] = ..., fully_consistent: bool = ...) -> None: ...

class RelationshipFilter(_message.Message):
    __slots__ = ("resource_type", "optional_resource_id", "optional_resource_id_prefix", "optional_relation", "optional_subject_filter")
    RESOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_RESOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_RESOURCE_ID_PREFIX_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_RELATION_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_SUBJECT_FILTER_FIELD_NUMBER: _ClassVar[int]
    resource_type: str
    optional_resource_id: str
    optional_resource_id_prefix: str
    optional_relation: str
    optional_subject_filter: SubjectFilter
    def __init__(self, resource_type: _Optional[str] = ..., optional_resource_id: _Optional[str] = ..., optional_resource_id_prefix: _Optional[str] = ..., optional_relation: _Optional[str] = ..., optional_subject_filter: _Optional[_Union[SubjectFilter, _Mapping]] = ...) -> None: ...

class SubjectFilter(_message.Message):
    __slots__ = ("subject_type", "optional_subject_id", "optional_relation")
    class RelationFilter(_message.Message):
        __slots__ = ("relation",)
        RELATION_FIELD_NUMBER: _ClassVar[int]
        relation: str
        def __init__(self, relation: _Optional[str] = ...) -> None: ...
    SUBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_SUBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_RELATION_FIELD_NUMBER: _ClassVar[int]
    subject_type: str
    optional_subject_id: str
    optional_relation: SubjectFilter.RelationFilter
    def __init__(self, subject_type: _Optional[str] = ..., optional_subject_id: _Optional[str] = ..., optional_relation: _Optional[_Union[SubjectFilter.RelationFilter, _Mapping]] = ...) -> None: ...

class ReadRelationshipsRequest(_message.Message):
    __slots__ = ("consistency", "relationship_filter", "optional_limit", "optional_cursor")
    CONSISTENCY_FIELD_NUMBER: _ClassVar[int]
    RELATIONSHIP_FILTER_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_LIMIT_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_CURSOR_FIELD_NUMBER: _ClassVar[int]
    consistency: Consistency
    relationship_filter: RelationshipFilter
    optional_limit: int
    optional_cursor: _core_pb2.Cursor
    def __init__(self, consistency: _Optional[_Union[Consistency, _Mapping]] = ..., relationship_filter: _Optional[_Union[RelationshipFilter, _Mapping]] = ..., optional_limit: _Optional[int] = ..., optional_cursor: _Optional[_Union[_core_pb2.Cursor, _Mapping]] = ...) -> None: ...

class ReadRelationshipsResponse(_message.Message):
    __slots__ = ("read_at", "relationship", "after_result_cursor")
    READ_AT_FIELD_NUMBER: _ClassVar[int]
    RELATIONSHIP_FIELD_NUMBER: _ClassVar[int]
    AFTER_RESULT_CURSOR_FIELD_NUMBER: _ClassVar[int]
    read_at: _core_pb2.ZedToken
    relationship: _core_pb2.Relationship
    after_result_cursor: _core_pb2.Cursor
    def __init__(self, read_at: _Optional[_Union[_core_pb2.ZedToken, _Mapping]] = ..., relationship: _Optional[_Union[_core_pb2.Relationship, _Mapping]] = ..., after_result_cursor: _Optional[_Union[_core_pb2.Cursor, _Mapping]] = ...) -> None: ...

class Precondition(_message.Message):
    __slots__ = ("operation", "filter")
    class Operation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OPERATION_UNSPECIFIED: _ClassVar[Precondition.Operation]
        OPERATION_MUST_NOT_MATCH: _ClassVar[Precondition.Operation]
        OPERATION_MUST_MATCH: _ClassVar[Precondition.Operation]
    OPERATION_UNSPECIFIED: Precondition.Operation
    OPERATION_MUST_NOT_MATCH: Precondition.Operation
    OPERATION_MUST_MATCH: Precondition.Operation
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    operation: Precondition.Operation
    filter: RelationshipFilter
    def __init__(self, operation: _Optional[_Union[Precondition.Operation, str]] = ..., filter: _Optional[_Union[RelationshipFilter, _Mapping]] = ...) -> None: ...

class WriteRelationshipsRequest(_message.Message):
    __slots__ = ("updates", "optional_preconditions")
    UPDATES_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_PRECONDITIONS_FIELD_NUMBER: _ClassVar[int]
    updates: _containers.RepeatedCompositeFieldContainer[_core_pb2.RelationshipUpdate]
    optional_preconditions: _containers.RepeatedCompositeFieldContainer[Precondition]
    def __init__(self, updates: _Optional[_Iterable[_Union[_core_pb2.RelationshipUpdate, _Mapping]]] = ..., optional_preconditions: _Optional[_Iterable[_Union[Precondition, _Mapping]]] = ...) -> None: ...

class WriteRelationshipsResponse(_message.Message):
    __slots__ = ("written_at",)
    WRITTEN_AT_FIELD_NUMBER: _ClassVar[int]
    written_at: _core_pb2.ZedToken
    def __init__(self, written_at: _Optional[_Union[_core_pb2.ZedToken, _Mapping]] = ...) -> None: ...

class DeleteRelationshipsRequest(_message.Message):
    __slots__ = ("relationship_filter", "optional_preconditions", "optional_limit", "optional_allow_partial_deletions")
    RELATIONSHIP_FILTER_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_PRECONDITIONS_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_LIMIT_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_ALLOW_PARTIAL_DELETIONS_FIELD_NUMBER: _ClassVar[int]
    relationship_filter: RelationshipFilter
    optional_preconditions: _containers.RepeatedCompositeFieldContainer[Precondition]
    optional_limit: int
    optional_allow_partial_deletions: bool
    def __init__(self, relationship_filter: _Optional[_Union[RelationshipFilter, _Mapping]] = ..., optional_preconditions: _Optional[_Iterable[_Union[Precondition, _Mapping]]] = ..., optional_limit: _Optional[int] = ..., optional_allow_partial_deletions: bool = ...) -> None: ...

class DeleteRelationshipsResponse(_message.Message):
    __slots__ = ("deleted_at", "deletion_progress")
    class DeletionProgress(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DELETION_PROGRESS_UNSPECIFIED: _ClassVar[DeleteRelationshipsResponse.DeletionProgress]
        DELETION_PROGRESS_COMPLETE: _ClassVar[DeleteRelationshipsResponse.DeletionProgress]
        DELETION_PROGRESS_PARTIAL: _ClassVar[DeleteRelationshipsResponse.DeletionProgress]
    DELETION_PROGRESS_UNSPECIFIED: DeleteRelationshipsResponse.DeletionProgress
    DELETION_PROGRESS_COMPLETE: DeleteRelationshipsResponse.DeletionProgress
    DELETION_PROGRESS_PARTIAL: DeleteRelationshipsResponse.DeletionProgress
    DELETED_AT_FIELD_NUMBER: _ClassVar[int]
    DELETION_PROGRESS_FIELD_NUMBER: _ClassVar[int]
    deleted_at: _core_pb2.ZedToken
    deletion_progress: DeleteRelationshipsResponse.DeletionProgress
    def __init__(self, deleted_at: _Optional[_Union[_core_pb2.ZedToken, _Mapping]] = ..., deletion_progress: _Optional[_Union[DeleteRelationshipsResponse.DeletionProgress, str]] = ...) -> None: ...

class CheckPermissionRequest(_message.Message):
    __slots__ = ("consistency", "resource", "permission", "subject", "context", "with_tracing")
    CONSISTENCY_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    WITH_TRACING_FIELD_NUMBER: _ClassVar[int]
    consistency: Consistency
    resource: _core_pb2.ObjectReference
    permission: str
    subject: _core_pb2.SubjectReference
    context: _struct_pb2.Struct
    with_tracing: bool
    def __init__(self, consistency: _Optional[_Union[Consistency, _Mapping]] = ..., resource: _Optional[_Union[_core_pb2.ObjectReference, _Mapping]] = ..., permission: _Optional[str] = ..., subject: _Optional[_Union[_core_pb2.SubjectReference, _Mapping]] = ..., context: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., with_tracing: bool = ...) -> None: ...

class CheckPermissionResponse(_message.Message):
    __slots__ = ("checked_at", "permissionship", "partial_caveat_info", "debug_trace")
    class Permissionship(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PERMISSIONSHIP_UNSPECIFIED: _ClassVar[CheckPermissionResponse.Permissionship]
        PERMISSIONSHIP_NO_PERMISSION: _ClassVar[CheckPermissionResponse.Permissionship]
        PERMISSIONSHIP_HAS_PERMISSION: _ClassVar[CheckPermissionResponse.Permissionship]
        PERMISSIONSHIP_CONDITIONAL_PERMISSION: _ClassVar[CheckPermissionResponse.Permissionship]
    PERMISSIONSHIP_UNSPECIFIED: CheckPermissionResponse.Permissionship
    PERMISSIONSHIP_NO_PERMISSION: CheckPermissionResponse.Permissionship
    PERMISSIONSHIP_HAS_PERMISSION: CheckPermissionResponse.Permissionship
    PERMISSIONSHIP_CONDITIONAL_PERMISSION: CheckPermissionResponse.Permissionship
    CHECKED_AT_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONSHIP_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_CAVEAT_INFO_FIELD_NUMBER: _ClassVar[int]
    DEBUG_TRACE_FIELD_NUMBER: _ClassVar[int]
    checked_at: _core_pb2.ZedToken
    permissionship: CheckPermissionResponse.Permissionship
    partial_caveat_info: _core_pb2.PartialCaveatInfo
    debug_trace: _debug_pb2.DebugInformation
    def __init__(self, checked_at: _Optional[_Union[_core_pb2.ZedToken, _Mapping]] = ..., permissionship: _Optional[_Union[CheckPermissionResponse.Permissionship, str]] = ..., partial_caveat_info: _Optional[_Union[_core_pb2.PartialCaveatInfo, _Mapping]] = ..., debug_trace: _Optional[_Union[_debug_pb2.DebugInformation, _Mapping]] = ...) -> None: ...

class CheckBulkPermissionsRequest(_message.Message):
    __slots__ = ("consistency", "items")
    CONSISTENCY_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    consistency: Consistency
    items: _containers.RepeatedCompositeFieldContainer[CheckBulkPermissionsRequestItem]
    def __init__(self, consistency: _Optional[_Union[Consistency, _Mapping]] = ..., items: _Optional[_Iterable[_Union[CheckBulkPermissionsRequestItem, _Mapping]]] = ...) -> None: ...

class CheckBulkPermissionsRequestItem(_message.Message):
    __slots__ = ("resource", "permission", "subject", "context")
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    resource: _core_pb2.ObjectReference
    permission: str
    subject: _core_pb2.SubjectReference
    context: _struct_pb2.Struct
    def __init__(self, resource: _Optional[_Union[_core_pb2.ObjectReference, _Mapping]] = ..., permission: _Optional[str] = ..., subject: _Optional[_Union[_core_pb2.SubjectReference, _Mapping]] = ..., context: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class CheckBulkPermissionsResponse(_message.Message):
    __slots__ = ("checked_at", "pairs")
    CHECKED_AT_FIELD_NUMBER: _ClassVar[int]
    PAIRS_FIELD_NUMBER: _ClassVar[int]
    checked_at: _core_pb2.ZedToken
    pairs: _containers.RepeatedCompositeFieldContainer[CheckBulkPermissionsPair]
    def __init__(self, checked_at: _Optional[_Union[_core_pb2.ZedToken, _Mapping]] = ..., pairs: _Optional[_Iterable[_Union[CheckBulkPermissionsPair, _Mapping]]] = ...) -> None: ...

class CheckBulkPermissionsPair(_message.Message):
    __slots__ = ("request", "item", "error")
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    ITEM_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    request: CheckBulkPermissionsRequestItem
    item: CheckBulkPermissionsResponseItem
    error: _status_pb2.Status
    def __init__(self, request: _Optional[_Union[CheckBulkPermissionsRequestItem, _Mapping]] = ..., item: _Optional[_Union[CheckBulkPermissionsResponseItem, _Mapping]] = ..., error: _Optional[_Union[_status_pb2.Status, _Mapping]] = ...) -> None: ...

class CheckBulkPermissionsResponseItem(_message.Message):
    __slots__ = ("permissionship", "partial_caveat_info")
    PERMISSIONSHIP_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_CAVEAT_INFO_FIELD_NUMBER: _ClassVar[int]
    permissionship: CheckPermissionResponse.Permissionship
    partial_caveat_info: _core_pb2.PartialCaveatInfo
    def __init__(self, permissionship: _Optional[_Union[CheckPermissionResponse.Permissionship, str]] = ..., partial_caveat_info: _Optional[_Union[_core_pb2.PartialCaveatInfo, _Mapping]] = ...) -> None: ...

class ExpandPermissionTreeRequest(_message.Message):
    __slots__ = ("consistency", "resource", "permission")
    CONSISTENCY_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_FIELD_NUMBER: _ClassVar[int]
    consistency: Consistency
    resource: _core_pb2.ObjectReference
    permission: str
    def __init__(self, consistency: _Optional[_Union[Consistency, _Mapping]] = ..., resource: _Optional[_Union[_core_pb2.ObjectReference, _Mapping]] = ..., permission: _Optional[str] = ...) -> None: ...

class ExpandPermissionTreeResponse(_message.Message):
    __slots__ = ("expanded_at", "tree_root")
    EXPANDED_AT_FIELD_NUMBER: _ClassVar[int]
    TREE_ROOT_FIELD_NUMBER: _ClassVar[int]
    expanded_at: _core_pb2.ZedToken
    tree_root: _core_pb2.PermissionRelationshipTree
    def __init__(self, expanded_at: _Optional[_Union[_core_pb2.ZedToken, _Mapping]] = ..., tree_root: _Optional[_Union[_core_pb2.PermissionRelationshipTree, _Mapping]] = ...) -> None: ...

class LookupResourcesRequest(_message.Message):
    __slots__ = ("consistency", "resource_object_type", "permission", "subject", "context", "optional_limit", "optional_cursor")
    CONSISTENCY_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_LIMIT_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_CURSOR_FIELD_NUMBER: _ClassVar[int]
    consistency: Consistency
    resource_object_type: str
    permission: str
    subject: _core_pb2.SubjectReference
    context: _struct_pb2.Struct
    optional_limit: int
    optional_cursor: _core_pb2.Cursor
    def __init__(self, consistency: _Optional[_Union[Consistency, _Mapping]] = ..., resource_object_type: _Optional[str] = ..., permission: _Optional[str] = ..., subject: _Optional[_Union[_core_pb2.SubjectReference, _Mapping]] = ..., context: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., optional_limit: _Optional[int] = ..., optional_cursor: _Optional[_Union[_core_pb2.Cursor, _Mapping]] = ...) -> None: ...

class LookupResourcesResponse(_message.Message):
    __slots__ = ("looked_up_at", "resource_object_id", "permissionship", "partial_caveat_info", "after_result_cursor")
    LOOKED_UP_AT_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONSHIP_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_CAVEAT_INFO_FIELD_NUMBER: _ClassVar[int]
    AFTER_RESULT_CURSOR_FIELD_NUMBER: _ClassVar[int]
    looked_up_at: _core_pb2.ZedToken
    resource_object_id: str
    permissionship: LookupPermissionship
    partial_caveat_info: _core_pb2.PartialCaveatInfo
    after_result_cursor: _core_pb2.Cursor
    def __init__(self, looked_up_at: _Optional[_Union[_core_pb2.ZedToken, _Mapping]] = ..., resource_object_id: _Optional[str] = ..., permissionship: _Optional[_Union[LookupPermissionship, str]] = ..., partial_caveat_info: _Optional[_Union[_core_pb2.PartialCaveatInfo, _Mapping]] = ..., after_result_cursor: _Optional[_Union[_core_pb2.Cursor, _Mapping]] = ...) -> None: ...

class LookupSubjectsRequest(_message.Message):
    __slots__ = ("consistency", "resource", "permission", "subject_object_type", "optional_subject_relation", "context", "optional_concrete_limit", "optional_cursor", "wildcard_option")
    class WildcardOption(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        WILDCARD_OPTION_UNSPECIFIED: _ClassVar[LookupSubjectsRequest.WildcardOption]
        WILDCARD_OPTION_INCLUDE_WILDCARDS: _ClassVar[LookupSubjectsRequest.WildcardOption]
        WILDCARD_OPTION_EXCLUDE_WILDCARDS: _ClassVar[LookupSubjectsRequest.WildcardOption]
    WILDCARD_OPTION_UNSPECIFIED: LookupSubjectsRequest.WildcardOption
    WILDCARD_OPTION_INCLUDE_WILDCARDS: LookupSubjectsRequest.WildcardOption
    WILDCARD_OPTION_EXCLUDE_WILDCARDS: LookupSubjectsRequest.WildcardOption
    CONSISTENCY_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_OBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_SUBJECT_RELATION_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_CONCRETE_LIMIT_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_CURSOR_FIELD_NUMBER: _ClassVar[int]
    WILDCARD_OPTION_FIELD_NUMBER: _ClassVar[int]
    consistency: Consistency
    resource: _core_pb2.ObjectReference
    permission: str
    subject_object_type: str
    optional_subject_relation: str
    context: _struct_pb2.Struct
    optional_concrete_limit: int
    optional_cursor: _core_pb2.Cursor
    wildcard_option: LookupSubjectsRequest.WildcardOption
    def __init__(self, consistency: _Optional[_Union[Consistency, _Mapping]] = ..., resource: _Optional[_Union[_core_pb2.ObjectReference, _Mapping]] = ..., permission: _Optional[str] = ..., subject_object_type: _Optional[str] = ..., optional_subject_relation: _Optional[str] = ..., context: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., optional_concrete_limit: _Optional[int] = ..., optional_cursor: _Optional[_Union[_core_pb2.Cursor, _Mapping]] = ..., wildcard_option: _Optional[_Union[LookupSubjectsRequest.WildcardOption, str]] = ...) -> None: ...

class LookupSubjectsResponse(_message.Message):
    __slots__ = ("looked_up_at", "subject_object_id", "excluded_subject_ids", "permissionship", "partial_caveat_info", "subject", "excluded_subjects", "after_result_cursor")
    LOOKED_UP_AT_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_SUBJECT_IDS_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONSHIP_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_CAVEAT_INFO_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    EXCLUDED_SUBJECTS_FIELD_NUMBER: _ClassVar[int]
    AFTER_RESULT_CURSOR_FIELD_NUMBER: _ClassVar[int]
    looked_up_at: _core_pb2.ZedToken
    subject_object_id: str
    excluded_subject_ids: _containers.RepeatedScalarFieldContainer[str]
    permissionship: LookupPermissionship
    partial_caveat_info: _core_pb2.PartialCaveatInfo
    subject: ResolvedSubject
    excluded_subjects: _containers.RepeatedCompositeFieldContainer[ResolvedSubject]
    after_result_cursor: _core_pb2.Cursor
    def __init__(self, looked_up_at: _Optional[_Union[_core_pb2.ZedToken, _Mapping]] = ..., subject_object_id: _Optional[str] = ..., excluded_subject_ids: _Optional[_Iterable[str]] = ..., permissionship: _Optional[_Union[LookupPermissionship, str]] = ..., partial_caveat_info: _Optional[_Union[_core_pb2.PartialCaveatInfo, _Mapping]] = ..., subject: _Optional[_Union[ResolvedSubject, _Mapping]] = ..., excluded_subjects: _Optional[_Iterable[_Union[ResolvedSubject, _Mapping]]] = ..., after_result_cursor: _Optional[_Union[_core_pb2.Cursor, _Mapping]] = ...) -> None: ...

class ResolvedSubject(_message.Message):
    __slots__ = ("subject_object_id", "permissionship", "partial_caveat_info")
    SUBJECT_OBJECT_ID_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONSHIP_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_CAVEAT_INFO_FIELD_NUMBER: _ClassVar[int]
    subject_object_id: str
    permissionship: LookupPermissionship
    partial_caveat_info: _core_pb2.PartialCaveatInfo
    def __init__(self, subject_object_id: _Optional[str] = ..., permissionship: _Optional[_Union[LookupPermissionship, str]] = ..., partial_caveat_info: _Optional[_Union[_core_pb2.PartialCaveatInfo, _Mapping]] = ...) -> None: ...
