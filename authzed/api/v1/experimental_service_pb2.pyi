from google.api import annotations_pb2 as _annotations_pb2
from validate import validate_pb2 as _validate_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.rpc import status_pb2 as _status_pb2
from authzed.api.v1 import core_pb2 as _core_pb2
from authzed.api.v1 import permission_service_pb2 as _permission_service_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ExperimentalRegisterRelationshipCounterRequest(_message.Message):
    __slots__ = ("name", "relationship_filter")
    NAME_FIELD_NUMBER: _ClassVar[int]
    RELATIONSHIP_FILTER_FIELD_NUMBER: _ClassVar[int]
    name: str
    relationship_filter: _permission_service_pb2.RelationshipFilter
    def __init__(self, name: _Optional[str] = ..., relationship_filter: _Optional[_Union[_permission_service_pb2.RelationshipFilter, _Mapping]] = ...) -> None: ...

class ExperimentalRegisterRelationshipCounterResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ExperimentalCountRelationshipsRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ExperimentalCountRelationshipsResponse(_message.Message):
    __slots__ = ("counter_still_calculating", "read_counter_value")
    COUNTER_STILL_CALCULATING_FIELD_NUMBER: _ClassVar[int]
    READ_COUNTER_VALUE_FIELD_NUMBER: _ClassVar[int]
    counter_still_calculating: bool
    read_counter_value: ReadCounterValue
    def __init__(self, counter_still_calculating: bool = ..., read_counter_value: _Optional[_Union[ReadCounterValue, _Mapping]] = ...) -> None: ...

class ReadCounterValue(_message.Message):
    __slots__ = ("relationship_count", "read_at")
    RELATIONSHIP_COUNT_FIELD_NUMBER: _ClassVar[int]
    READ_AT_FIELD_NUMBER: _ClassVar[int]
    relationship_count: int
    read_at: _core_pb2.ZedToken
    def __init__(self, relationship_count: _Optional[int] = ..., read_at: _Optional[_Union[_core_pb2.ZedToken, _Mapping]] = ...) -> None: ...

class ExperimentalUnregisterRelationshipCounterRequest(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class ExperimentalUnregisterRelationshipCounterResponse(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class BulkCheckPermissionRequest(_message.Message):
    __slots__ = ("consistency", "items")
    CONSISTENCY_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    consistency: _permission_service_pb2.Consistency
    items: _containers.RepeatedCompositeFieldContainer[BulkCheckPermissionRequestItem]
    def __init__(self, consistency: _Optional[_Union[_permission_service_pb2.Consistency, _Mapping]] = ..., items: _Optional[_Iterable[_Union[BulkCheckPermissionRequestItem, _Mapping]]] = ...) -> None: ...

class BulkCheckPermissionRequestItem(_message.Message):
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

class BulkCheckPermissionResponse(_message.Message):
    __slots__ = ("checked_at", "pairs")
    CHECKED_AT_FIELD_NUMBER: _ClassVar[int]
    PAIRS_FIELD_NUMBER: _ClassVar[int]
    checked_at: _core_pb2.ZedToken
    pairs: _containers.RepeatedCompositeFieldContainer[BulkCheckPermissionPair]
    def __init__(self, checked_at: _Optional[_Union[_core_pb2.ZedToken, _Mapping]] = ..., pairs: _Optional[_Iterable[_Union[BulkCheckPermissionPair, _Mapping]]] = ...) -> None: ...

class BulkCheckPermissionPair(_message.Message):
    __slots__ = ("request", "item", "error")
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    ITEM_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    request: BulkCheckPermissionRequestItem
    item: BulkCheckPermissionResponseItem
    error: _status_pb2.Status
    def __init__(self, request: _Optional[_Union[BulkCheckPermissionRequestItem, _Mapping]] = ..., item: _Optional[_Union[BulkCheckPermissionResponseItem, _Mapping]] = ..., error: _Optional[_Union[_status_pb2.Status, _Mapping]] = ...) -> None: ...

class BulkCheckPermissionResponseItem(_message.Message):
    __slots__ = ("permissionship", "partial_caveat_info")
    PERMISSIONSHIP_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_CAVEAT_INFO_FIELD_NUMBER: _ClassVar[int]
    permissionship: _permission_service_pb2.CheckPermissionResponse.Permissionship
    partial_caveat_info: _core_pb2.PartialCaveatInfo
    def __init__(self, permissionship: _Optional[_Union[_permission_service_pb2.CheckPermissionResponse.Permissionship, str]] = ..., partial_caveat_info: _Optional[_Union[_core_pb2.PartialCaveatInfo, _Mapping]] = ...) -> None: ...

class BulkImportRelationshipsRequest(_message.Message):
    __slots__ = ("relationships",)
    RELATIONSHIPS_FIELD_NUMBER: _ClassVar[int]
    relationships: _containers.RepeatedCompositeFieldContainer[_core_pb2.Relationship]
    def __init__(self, relationships: _Optional[_Iterable[_Union[_core_pb2.Relationship, _Mapping]]] = ...) -> None: ...

class BulkImportRelationshipsResponse(_message.Message):
    __slots__ = ("num_loaded",)
    NUM_LOADED_FIELD_NUMBER: _ClassVar[int]
    num_loaded: int
    def __init__(self, num_loaded: _Optional[int] = ...) -> None: ...

class BulkExportRelationshipsRequest(_message.Message):
    __slots__ = ("consistency", "optional_limit", "optional_cursor", "optional_relationship_filter")
    CONSISTENCY_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_LIMIT_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_CURSOR_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_RELATIONSHIP_FILTER_FIELD_NUMBER: _ClassVar[int]
    consistency: _permission_service_pb2.Consistency
    optional_limit: int
    optional_cursor: _core_pb2.Cursor
    optional_relationship_filter: _permission_service_pb2.RelationshipFilter
    def __init__(self, consistency: _Optional[_Union[_permission_service_pb2.Consistency, _Mapping]] = ..., optional_limit: _Optional[int] = ..., optional_cursor: _Optional[_Union[_core_pb2.Cursor, _Mapping]] = ..., optional_relationship_filter: _Optional[_Union[_permission_service_pb2.RelationshipFilter, _Mapping]] = ...) -> None: ...

class BulkExportRelationshipsResponse(_message.Message):
    __slots__ = ("after_result_cursor", "relationships")
    AFTER_RESULT_CURSOR_FIELD_NUMBER: _ClassVar[int]
    RELATIONSHIPS_FIELD_NUMBER: _ClassVar[int]
    after_result_cursor: _core_pb2.Cursor
    relationships: _containers.RepeatedCompositeFieldContainer[_core_pb2.Relationship]
    def __init__(self, after_result_cursor: _Optional[_Union[_core_pb2.Cursor, _Mapping]] = ..., relationships: _Optional[_Iterable[_Union[_core_pb2.Relationship, _Mapping]]] = ...) -> None: ...

class ExperimentalReflectSchemaRequest(_message.Message):
    __slots__ = ("consistency", "optional_filters")
    CONSISTENCY_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_FILTERS_FIELD_NUMBER: _ClassVar[int]
    consistency: _permission_service_pb2.Consistency
    optional_filters: _containers.RepeatedCompositeFieldContainer[ExpSchemaFilter]
    def __init__(self, consistency: _Optional[_Union[_permission_service_pb2.Consistency, _Mapping]] = ..., optional_filters: _Optional[_Iterable[_Union[ExpSchemaFilter, _Mapping]]] = ...) -> None: ...

class ExperimentalReflectSchemaResponse(_message.Message):
    __slots__ = ("definitions", "caveats", "read_at")
    DEFINITIONS_FIELD_NUMBER: _ClassVar[int]
    CAVEATS_FIELD_NUMBER: _ClassVar[int]
    READ_AT_FIELD_NUMBER: _ClassVar[int]
    definitions: _containers.RepeatedCompositeFieldContainer[ExpDefinition]
    caveats: _containers.RepeatedCompositeFieldContainer[ExpCaveat]
    read_at: _core_pb2.ZedToken
    def __init__(self, definitions: _Optional[_Iterable[_Union[ExpDefinition, _Mapping]]] = ..., caveats: _Optional[_Iterable[_Union[ExpCaveat, _Mapping]]] = ..., read_at: _Optional[_Union[_core_pb2.ZedToken, _Mapping]] = ...) -> None: ...

class ExpSchemaFilter(_message.Message):
    __slots__ = ("optional_definition_name_filter", "optional_caveat_name_filter", "optional_relation_name_filter", "optional_permission_name_filter")
    OPTIONAL_DEFINITION_NAME_FILTER_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_CAVEAT_NAME_FILTER_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_RELATION_NAME_FILTER_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_PERMISSION_NAME_FILTER_FIELD_NUMBER: _ClassVar[int]
    optional_definition_name_filter: str
    optional_caveat_name_filter: str
    optional_relation_name_filter: str
    optional_permission_name_filter: str
    def __init__(self, optional_definition_name_filter: _Optional[str] = ..., optional_caveat_name_filter: _Optional[str] = ..., optional_relation_name_filter: _Optional[str] = ..., optional_permission_name_filter: _Optional[str] = ...) -> None: ...

class ExpDefinition(_message.Message):
    __slots__ = ("name", "comment", "relations", "permissions")
    NAME_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    RELATIONS_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    comment: str
    relations: _containers.RepeatedCompositeFieldContainer[ExpRelation]
    permissions: _containers.RepeatedCompositeFieldContainer[ExpPermission]
    def __init__(self, name: _Optional[str] = ..., comment: _Optional[str] = ..., relations: _Optional[_Iterable[_Union[ExpRelation, _Mapping]]] = ..., permissions: _Optional[_Iterable[_Union[ExpPermission, _Mapping]]] = ...) -> None: ...

class ExpCaveat(_message.Message):
    __slots__ = ("name", "comment", "parameters", "expression")
    NAME_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    name: str
    comment: str
    parameters: _containers.RepeatedCompositeFieldContainer[ExpCaveatParameter]
    expression: str
    def __init__(self, name: _Optional[str] = ..., comment: _Optional[str] = ..., parameters: _Optional[_Iterable[_Union[ExpCaveatParameter, _Mapping]]] = ..., expression: _Optional[str] = ...) -> None: ...

class ExpCaveatParameter(_message.Message):
    __slots__ = ("name", "type", "parent_caveat_name")
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PARENT_CAVEAT_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: str
    parent_caveat_name: str
    def __init__(self, name: _Optional[str] = ..., type: _Optional[str] = ..., parent_caveat_name: _Optional[str] = ...) -> None: ...

class ExpRelation(_message.Message):
    __slots__ = ("name", "comment", "parent_definition_name", "subject_types")
    NAME_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    PARENT_DEFINITION_NAME_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_TYPES_FIELD_NUMBER: _ClassVar[int]
    name: str
    comment: str
    parent_definition_name: str
    subject_types: _containers.RepeatedCompositeFieldContainer[ExpTypeReference]
    def __init__(self, name: _Optional[str] = ..., comment: _Optional[str] = ..., parent_definition_name: _Optional[str] = ..., subject_types: _Optional[_Iterable[_Union[ExpTypeReference, _Mapping]]] = ...) -> None: ...

class ExpTypeReference(_message.Message):
    __slots__ = ("subject_definition_name", "optional_caveat_name", "is_terminal_subject", "optional_relation_name", "is_public_wildcard")
    SUBJECT_DEFINITION_NAME_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_CAVEAT_NAME_FIELD_NUMBER: _ClassVar[int]
    IS_TERMINAL_SUBJECT_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_RELATION_NAME_FIELD_NUMBER: _ClassVar[int]
    IS_PUBLIC_WILDCARD_FIELD_NUMBER: _ClassVar[int]
    subject_definition_name: str
    optional_caveat_name: str
    is_terminal_subject: bool
    optional_relation_name: str
    is_public_wildcard: bool
    def __init__(self, subject_definition_name: _Optional[str] = ..., optional_caveat_name: _Optional[str] = ..., is_terminal_subject: bool = ..., optional_relation_name: _Optional[str] = ..., is_public_wildcard: bool = ...) -> None: ...

class ExpPermission(_message.Message):
    __slots__ = ("name", "comment", "parent_definition_name")
    NAME_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    PARENT_DEFINITION_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    comment: str
    parent_definition_name: str
    def __init__(self, name: _Optional[str] = ..., comment: _Optional[str] = ..., parent_definition_name: _Optional[str] = ...) -> None: ...

class ExperimentalComputablePermissionsRequest(_message.Message):
    __slots__ = ("consistency", "definition_name", "relation_name", "optional_definition_name_filter")
    CONSISTENCY_FIELD_NUMBER: _ClassVar[int]
    DEFINITION_NAME_FIELD_NUMBER: _ClassVar[int]
    RELATION_NAME_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_DEFINITION_NAME_FILTER_FIELD_NUMBER: _ClassVar[int]
    consistency: _permission_service_pb2.Consistency
    definition_name: str
    relation_name: str
    optional_definition_name_filter: str
    def __init__(self, consistency: _Optional[_Union[_permission_service_pb2.Consistency, _Mapping]] = ..., definition_name: _Optional[str] = ..., relation_name: _Optional[str] = ..., optional_definition_name_filter: _Optional[str] = ...) -> None: ...

class ExpRelationReference(_message.Message):
    __slots__ = ("definition_name", "relation_name", "is_permission")
    DEFINITION_NAME_FIELD_NUMBER: _ClassVar[int]
    RELATION_NAME_FIELD_NUMBER: _ClassVar[int]
    IS_PERMISSION_FIELD_NUMBER: _ClassVar[int]
    definition_name: str
    relation_name: str
    is_permission: bool
    def __init__(self, definition_name: _Optional[str] = ..., relation_name: _Optional[str] = ..., is_permission: bool = ...) -> None: ...

class ExperimentalComputablePermissionsResponse(_message.Message):
    __slots__ = ("permissions", "read_at")
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    READ_AT_FIELD_NUMBER: _ClassVar[int]
    permissions: _containers.RepeatedCompositeFieldContainer[ExpRelationReference]
    read_at: _core_pb2.ZedToken
    def __init__(self, permissions: _Optional[_Iterable[_Union[ExpRelationReference, _Mapping]]] = ..., read_at: _Optional[_Union[_core_pb2.ZedToken, _Mapping]] = ...) -> None: ...

class ExperimentalDependentRelationsRequest(_message.Message):
    __slots__ = ("consistency", "definition_name", "permission_name")
    CONSISTENCY_FIELD_NUMBER: _ClassVar[int]
    DEFINITION_NAME_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_NAME_FIELD_NUMBER: _ClassVar[int]
    consistency: _permission_service_pb2.Consistency
    definition_name: str
    permission_name: str
    def __init__(self, consistency: _Optional[_Union[_permission_service_pb2.Consistency, _Mapping]] = ..., definition_name: _Optional[str] = ..., permission_name: _Optional[str] = ...) -> None: ...

class ExperimentalDependentRelationsResponse(_message.Message):
    __slots__ = ("relations", "read_at")
    RELATIONS_FIELD_NUMBER: _ClassVar[int]
    READ_AT_FIELD_NUMBER: _ClassVar[int]
    relations: _containers.RepeatedCompositeFieldContainer[ExpRelationReference]
    read_at: _core_pb2.ZedToken
    def __init__(self, relations: _Optional[_Iterable[_Union[ExpRelationReference, _Mapping]]] = ..., read_at: _Optional[_Union[_core_pb2.ZedToken, _Mapping]] = ...) -> None: ...

class ExperimentalDiffSchemaRequest(_message.Message):
    __slots__ = ("consistency", "comparison_schema")
    CONSISTENCY_FIELD_NUMBER: _ClassVar[int]
    COMPARISON_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    consistency: _permission_service_pb2.Consistency
    comparison_schema: str
    def __init__(self, consistency: _Optional[_Union[_permission_service_pb2.Consistency, _Mapping]] = ..., comparison_schema: _Optional[str] = ...) -> None: ...

class ExperimentalDiffSchemaResponse(_message.Message):
    __slots__ = ("diffs", "read_at")
    DIFFS_FIELD_NUMBER: _ClassVar[int]
    READ_AT_FIELD_NUMBER: _ClassVar[int]
    diffs: _containers.RepeatedCompositeFieldContainer[ExpSchemaDiff]
    read_at: _core_pb2.ZedToken
    def __init__(self, diffs: _Optional[_Iterable[_Union[ExpSchemaDiff, _Mapping]]] = ..., read_at: _Optional[_Union[_core_pb2.ZedToken, _Mapping]] = ...) -> None: ...

class ExpRelationSubjectTypeChange(_message.Message):
    __slots__ = ("relation", "changed_subject_type")
    RELATION_FIELD_NUMBER: _ClassVar[int]
    CHANGED_SUBJECT_TYPE_FIELD_NUMBER: _ClassVar[int]
    relation: ExpRelation
    changed_subject_type: ExpTypeReference
    def __init__(self, relation: _Optional[_Union[ExpRelation, _Mapping]] = ..., changed_subject_type: _Optional[_Union[ExpTypeReference, _Mapping]] = ...) -> None: ...

class ExpCaveatParameterTypeChange(_message.Message):
    __slots__ = ("parameter", "previous_type")
    PARAMETER_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_TYPE_FIELD_NUMBER: _ClassVar[int]
    parameter: ExpCaveatParameter
    previous_type: str
    def __init__(self, parameter: _Optional[_Union[ExpCaveatParameter, _Mapping]] = ..., previous_type: _Optional[str] = ...) -> None: ...

class ExpSchemaDiff(_message.Message):
    __slots__ = ("definition_added", "definition_removed", "definition_doc_comment_changed", "relation_added", "relation_removed", "relation_doc_comment_changed", "relation_subject_type_added", "relation_subject_type_removed", "permission_added", "permission_removed", "permission_doc_comment_changed", "permission_expr_changed", "caveat_added", "caveat_removed", "caveat_doc_comment_changed", "caveat_expr_changed", "caveat_parameter_added", "caveat_parameter_removed", "caveat_parameter_type_changed")
    DEFINITION_ADDED_FIELD_NUMBER: _ClassVar[int]
    DEFINITION_REMOVED_FIELD_NUMBER: _ClassVar[int]
    DEFINITION_DOC_COMMENT_CHANGED_FIELD_NUMBER: _ClassVar[int]
    RELATION_ADDED_FIELD_NUMBER: _ClassVar[int]
    RELATION_REMOVED_FIELD_NUMBER: _ClassVar[int]
    RELATION_DOC_COMMENT_CHANGED_FIELD_NUMBER: _ClassVar[int]
    RELATION_SUBJECT_TYPE_ADDED_FIELD_NUMBER: _ClassVar[int]
    RELATION_SUBJECT_TYPE_REMOVED_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_ADDED_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_REMOVED_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_DOC_COMMENT_CHANGED_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_EXPR_CHANGED_FIELD_NUMBER: _ClassVar[int]
    CAVEAT_ADDED_FIELD_NUMBER: _ClassVar[int]
    CAVEAT_REMOVED_FIELD_NUMBER: _ClassVar[int]
    CAVEAT_DOC_COMMENT_CHANGED_FIELD_NUMBER: _ClassVar[int]
    CAVEAT_EXPR_CHANGED_FIELD_NUMBER: _ClassVar[int]
    CAVEAT_PARAMETER_ADDED_FIELD_NUMBER: _ClassVar[int]
    CAVEAT_PARAMETER_REMOVED_FIELD_NUMBER: _ClassVar[int]
    CAVEAT_PARAMETER_TYPE_CHANGED_FIELD_NUMBER: _ClassVar[int]
    definition_added: ExpDefinition
    definition_removed: ExpDefinition
    definition_doc_comment_changed: ExpDefinition
    relation_added: ExpRelation
    relation_removed: ExpRelation
    relation_doc_comment_changed: ExpRelation
    relation_subject_type_added: ExpRelationSubjectTypeChange
    relation_subject_type_removed: ExpRelationSubjectTypeChange
    permission_added: ExpPermission
    permission_removed: ExpPermission
    permission_doc_comment_changed: ExpPermission
    permission_expr_changed: ExpPermission
    caveat_added: ExpCaveat
    caveat_removed: ExpCaveat
    caveat_doc_comment_changed: ExpCaveat
    caveat_expr_changed: ExpCaveat
    caveat_parameter_added: ExpCaveatParameter
    caveat_parameter_removed: ExpCaveatParameter
    caveat_parameter_type_changed: ExpCaveatParameterTypeChange
    def __init__(self, definition_added: _Optional[_Union[ExpDefinition, _Mapping]] = ..., definition_removed: _Optional[_Union[ExpDefinition, _Mapping]] = ..., definition_doc_comment_changed: _Optional[_Union[ExpDefinition, _Mapping]] = ..., relation_added: _Optional[_Union[ExpRelation, _Mapping]] = ..., relation_removed: _Optional[_Union[ExpRelation, _Mapping]] = ..., relation_doc_comment_changed: _Optional[_Union[ExpRelation, _Mapping]] = ..., relation_subject_type_added: _Optional[_Union[ExpRelationSubjectTypeChange, _Mapping]] = ..., relation_subject_type_removed: _Optional[_Union[ExpRelationSubjectTypeChange, _Mapping]] = ..., permission_added: _Optional[_Union[ExpPermission, _Mapping]] = ..., permission_removed: _Optional[_Union[ExpPermission, _Mapping]] = ..., permission_doc_comment_changed: _Optional[_Union[ExpPermission, _Mapping]] = ..., permission_expr_changed: _Optional[_Union[ExpPermission, _Mapping]] = ..., caveat_added: _Optional[_Union[ExpCaveat, _Mapping]] = ..., caveat_removed: _Optional[_Union[ExpCaveat, _Mapping]] = ..., caveat_doc_comment_changed: _Optional[_Union[ExpCaveat, _Mapping]] = ..., caveat_expr_changed: _Optional[_Union[ExpCaveat, _Mapping]] = ..., caveat_parameter_added: _Optional[_Union[ExpCaveatParameter, _Mapping]] = ..., caveat_parameter_removed: _Optional[_Union[ExpCaveatParameter, _Mapping]] = ..., caveat_parameter_type_changed: _Optional[_Union[ExpCaveatParameterTypeChange, _Mapping]] = ...) -> None: ...
