from authzed.api.v0 import core_pb2 as _core_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FormatSchemaRequest(_message.Message):
    __slots__ = ("schema",)
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    schema: str
    def __init__(self, schema: _Optional[str] = ...) -> None: ...

class FormatSchemaResponse(_message.Message):
    __slots__ = ("error", "formatted_schema")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    FORMATTED_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    error: DeveloperError
    formatted_schema: str
    def __init__(self, error: _Optional[_Union[DeveloperError, _Mapping]] = ..., formatted_schema: _Optional[str] = ...) -> None: ...

class UpgradeSchemaRequest(_message.Message):
    __slots__ = ("namespace_configs",)
    NAMESPACE_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    namespace_configs: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, namespace_configs: _Optional[_Iterable[str]] = ...) -> None: ...

class UpgradeSchemaResponse(_message.Message):
    __slots__ = ("error", "upgraded_schema")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    UPGRADED_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    error: DeveloperError
    upgraded_schema: str
    def __init__(self, error: _Optional[_Union[DeveloperError, _Mapping]] = ..., upgraded_schema: _Optional[str] = ...) -> None: ...

class ShareRequest(_message.Message):
    __slots__ = ("schema", "relationships_yaml", "validation_yaml", "assertions_yaml")
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    RELATIONSHIPS_YAML_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_YAML_FIELD_NUMBER: _ClassVar[int]
    ASSERTIONS_YAML_FIELD_NUMBER: _ClassVar[int]
    schema: str
    relationships_yaml: str
    validation_yaml: str
    assertions_yaml: str
    def __init__(self, schema: _Optional[str] = ..., relationships_yaml: _Optional[str] = ..., validation_yaml: _Optional[str] = ..., assertions_yaml: _Optional[str] = ...) -> None: ...

class ShareResponse(_message.Message):
    __slots__ = ("share_reference",)
    SHARE_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    share_reference: str
    def __init__(self, share_reference: _Optional[str] = ...) -> None: ...

class LookupShareRequest(_message.Message):
    __slots__ = ("share_reference",)
    SHARE_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    share_reference: str
    def __init__(self, share_reference: _Optional[str] = ...) -> None: ...

class LookupShareResponse(_message.Message):
    __slots__ = ("status", "schema", "relationships_yaml", "validation_yaml", "assertions_yaml")
    class LookupStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_REFERENCE: _ClassVar[LookupShareResponse.LookupStatus]
        FAILED_TO_LOOKUP: _ClassVar[LookupShareResponse.LookupStatus]
        VALID_REFERENCE: _ClassVar[LookupShareResponse.LookupStatus]
        UPGRADED_REFERENCE: _ClassVar[LookupShareResponse.LookupStatus]
    UNKNOWN_REFERENCE: LookupShareResponse.LookupStatus
    FAILED_TO_LOOKUP: LookupShareResponse.LookupStatus
    VALID_REFERENCE: LookupShareResponse.LookupStatus
    UPGRADED_REFERENCE: LookupShareResponse.LookupStatus
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    RELATIONSHIPS_YAML_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_YAML_FIELD_NUMBER: _ClassVar[int]
    ASSERTIONS_YAML_FIELD_NUMBER: _ClassVar[int]
    status: LookupShareResponse.LookupStatus
    schema: str
    relationships_yaml: str
    validation_yaml: str
    assertions_yaml: str
    def __init__(self, status: _Optional[_Union[LookupShareResponse.LookupStatus, str]] = ..., schema: _Optional[str] = ..., relationships_yaml: _Optional[str] = ..., validation_yaml: _Optional[str] = ..., assertions_yaml: _Optional[str] = ...) -> None: ...

class RequestContext(_message.Message):
    __slots__ = ("schema", "relationships")
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    RELATIONSHIPS_FIELD_NUMBER: _ClassVar[int]
    schema: str
    relationships: _containers.RepeatedCompositeFieldContainer[_core_pb2.RelationTuple]
    def __init__(self, schema: _Optional[str] = ..., relationships: _Optional[_Iterable[_Union[_core_pb2.RelationTuple, _Mapping]]] = ...) -> None: ...

class EditCheckRequest(_message.Message):
    __slots__ = ("context", "check_relationships")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    CHECK_RELATIONSHIPS_FIELD_NUMBER: _ClassVar[int]
    context: RequestContext
    check_relationships: _containers.RepeatedCompositeFieldContainer[_core_pb2.RelationTuple]
    def __init__(self, context: _Optional[_Union[RequestContext, _Mapping]] = ..., check_relationships: _Optional[_Iterable[_Union[_core_pb2.RelationTuple, _Mapping]]] = ...) -> None: ...

class EditCheckResult(_message.Message):
    __slots__ = ("relationship", "is_member", "error")
    RELATIONSHIP_FIELD_NUMBER: _ClassVar[int]
    IS_MEMBER_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    relationship: _core_pb2.RelationTuple
    is_member: bool
    error: DeveloperError
    def __init__(self, relationship: _Optional[_Union[_core_pb2.RelationTuple, _Mapping]] = ..., is_member: bool = ..., error: _Optional[_Union[DeveloperError, _Mapping]] = ...) -> None: ...

class EditCheckResponse(_message.Message):
    __slots__ = ("request_errors", "check_results")
    REQUEST_ERRORS_FIELD_NUMBER: _ClassVar[int]
    CHECK_RESULTS_FIELD_NUMBER: _ClassVar[int]
    request_errors: _containers.RepeatedCompositeFieldContainer[DeveloperError]
    check_results: _containers.RepeatedCompositeFieldContainer[EditCheckResult]
    def __init__(self, request_errors: _Optional[_Iterable[_Union[DeveloperError, _Mapping]]] = ..., check_results: _Optional[_Iterable[_Union[EditCheckResult, _Mapping]]] = ...) -> None: ...

class ValidateRequest(_message.Message):
    __slots__ = ("context", "validation_yaml", "update_validation_yaml", "assertions_yaml")
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_YAML_FIELD_NUMBER: _ClassVar[int]
    UPDATE_VALIDATION_YAML_FIELD_NUMBER: _ClassVar[int]
    ASSERTIONS_YAML_FIELD_NUMBER: _ClassVar[int]
    context: RequestContext
    validation_yaml: str
    update_validation_yaml: bool
    assertions_yaml: str
    def __init__(self, context: _Optional[_Union[RequestContext, _Mapping]] = ..., validation_yaml: _Optional[str] = ..., update_validation_yaml: bool = ..., assertions_yaml: _Optional[str] = ...) -> None: ...

class ValidateResponse(_message.Message):
    __slots__ = ("request_errors", "validation_errors", "updated_validation_yaml")
    REQUEST_ERRORS_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_ERRORS_FIELD_NUMBER: _ClassVar[int]
    UPDATED_VALIDATION_YAML_FIELD_NUMBER: _ClassVar[int]
    request_errors: _containers.RepeatedCompositeFieldContainer[DeveloperError]
    validation_errors: _containers.RepeatedCompositeFieldContainer[DeveloperError]
    updated_validation_yaml: str
    def __init__(self, request_errors: _Optional[_Iterable[_Union[DeveloperError, _Mapping]]] = ..., validation_errors: _Optional[_Iterable[_Union[DeveloperError, _Mapping]]] = ..., updated_validation_yaml: _Optional[str] = ...) -> None: ...

class DeveloperError(_message.Message):
    __slots__ = ("message", "line", "column", "source", "kind", "path", "context")
    class Source(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_SOURCE: _ClassVar[DeveloperError.Source]
        SCHEMA: _ClassVar[DeveloperError.Source]
        RELATIONSHIP: _ClassVar[DeveloperError.Source]
        VALIDATION_YAML: _ClassVar[DeveloperError.Source]
        CHECK_WATCH: _ClassVar[DeveloperError.Source]
        ASSERTION: _ClassVar[DeveloperError.Source]
    UNKNOWN_SOURCE: DeveloperError.Source
    SCHEMA: DeveloperError.Source
    RELATIONSHIP: DeveloperError.Source
    VALIDATION_YAML: DeveloperError.Source
    CHECK_WATCH: DeveloperError.Source
    ASSERTION: DeveloperError.Source
    class ErrorKind(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNKNOWN_KIND: _ClassVar[DeveloperError.ErrorKind]
        PARSE_ERROR: _ClassVar[DeveloperError.ErrorKind]
        SCHEMA_ISSUE: _ClassVar[DeveloperError.ErrorKind]
        DUPLICATE_RELATIONSHIP: _ClassVar[DeveloperError.ErrorKind]
        MISSING_EXPECTED_RELATIONSHIP: _ClassVar[DeveloperError.ErrorKind]
        EXTRA_RELATIONSHIP_FOUND: _ClassVar[DeveloperError.ErrorKind]
        UNKNOWN_OBJECT_TYPE: _ClassVar[DeveloperError.ErrorKind]
        UNKNOWN_RELATION: _ClassVar[DeveloperError.ErrorKind]
        MAXIMUM_RECURSION: _ClassVar[DeveloperError.ErrorKind]
        ASSERTION_FAILED: _ClassVar[DeveloperError.ErrorKind]
    UNKNOWN_KIND: DeveloperError.ErrorKind
    PARSE_ERROR: DeveloperError.ErrorKind
    SCHEMA_ISSUE: DeveloperError.ErrorKind
    DUPLICATE_RELATIONSHIP: DeveloperError.ErrorKind
    MISSING_EXPECTED_RELATIONSHIP: DeveloperError.ErrorKind
    EXTRA_RELATIONSHIP_FOUND: DeveloperError.ErrorKind
    UNKNOWN_OBJECT_TYPE: DeveloperError.ErrorKind
    UNKNOWN_RELATION: DeveloperError.ErrorKind
    MAXIMUM_RECURSION: DeveloperError.ErrorKind
    ASSERTION_FAILED: DeveloperError.ErrorKind
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    LINE_FIELD_NUMBER: _ClassVar[int]
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    KIND_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    message: str
    line: int
    column: int
    source: DeveloperError.Source
    kind: DeveloperError.ErrorKind
    path: _containers.RepeatedScalarFieldContainer[str]
    context: str
    def __init__(self, message: _Optional[str] = ..., line: _Optional[int] = ..., column: _Optional[int] = ..., source: _Optional[_Union[DeveloperError.Source, str]] = ..., kind: _Optional[_Union[DeveloperError.ErrorKind, str]] = ..., path: _Optional[_Iterable[str]] = ..., context: _Optional[str] = ...) -> None: ...
