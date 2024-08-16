from authzed.api.v1 import core_pb2 as _core_pb2
from validate import validate_pb2 as _validate_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DebugInformation(_message.Message):
    __slots__ = ("check", "schema_used")
    CHECK_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_USED_FIELD_NUMBER: _ClassVar[int]
    check: CheckDebugTrace
    schema_used: str
    def __init__(self, check: _Optional[_Union[CheckDebugTrace, _Mapping]] = ..., schema_used: _Optional[str] = ...) -> None: ...

class CheckDebugTrace(_message.Message):
    __slots__ = ("resource", "permission", "permission_type", "subject", "result", "caveat_evaluation_info", "duration", "was_cached_result", "sub_problems")
    class PermissionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PERMISSION_TYPE_UNSPECIFIED: _ClassVar[CheckDebugTrace.PermissionType]
        PERMISSION_TYPE_RELATION: _ClassVar[CheckDebugTrace.PermissionType]
        PERMISSION_TYPE_PERMISSION: _ClassVar[CheckDebugTrace.PermissionType]
    PERMISSION_TYPE_UNSPECIFIED: CheckDebugTrace.PermissionType
    PERMISSION_TYPE_RELATION: CheckDebugTrace.PermissionType
    PERMISSION_TYPE_PERMISSION: CheckDebugTrace.PermissionType
    class Permissionship(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PERMISSIONSHIP_UNSPECIFIED: _ClassVar[CheckDebugTrace.Permissionship]
        PERMISSIONSHIP_NO_PERMISSION: _ClassVar[CheckDebugTrace.Permissionship]
        PERMISSIONSHIP_HAS_PERMISSION: _ClassVar[CheckDebugTrace.Permissionship]
        PERMISSIONSHIP_CONDITIONAL_PERMISSION: _ClassVar[CheckDebugTrace.Permissionship]
    PERMISSIONSHIP_UNSPECIFIED: CheckDebugTrace.Permissionship
    PERMISSIONSHIP_NO_PERMISSION: CheckDebugTrace.Permissionship
    PERMISSIONSHIP_HAS_PERMISSION: CheckDebugTrace.Permissionship
    PERMISSIONSHIP_CONDITIONAL_PERMISSION: CheckDebugTrace.Permissionship
    class SubProblems(_message.Message):
        __slots__ = ("traces",)
        TRACES_FIELD_NUMBER: _ClassVar[int]
        traces: _containers.RepeatedCompositeFieldContainer[CheckDebugTrace]
        def __init__(self, traces: _Optional[_Iterable[_Union[CheckDebugTrace, _Mapping]]] = ...) -> None: ...
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_FIELD_NUMBER: _ClassVar[int]
    PERMISSION_TYPE_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    CAVEAT_EVALUATION_INFO_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    WAS_CACHED_RESULT_FIELD_NUMBER: _ClassVar[int]
    SUB_PROBLEMS_FIELD_NUMBER: _ClassVar[int]
    resource: _core_pb2.ObjectReference
    permission: str
    permission_type: CheckDebugTrace.PermissionType
    subject: _core_pb2.SubjectReference
    result: CheckDebugTrace.Permissionship
    caveat_evaluation_info: CaveatEvalInfo
    duration: _duration_pb2.Duration
    was_cached_result: bool
    sub_problems: CheckDebugTrace.SubProblems
    def __init__(self, resource: _Optional[_Union[_core_pb2.ObjectReference, _Mapping]] = ..., permission: _Optional[str] = ..., permission_type: _Optional[_Union[CheckDebugTrace.PermissionType, str]] = ..., subject: _Optional[_Union[_core_pb2.SubjectReference, _Mapping]] = ..., result: _Optional[_Union[CheckDebugTrace.Permissionship, str]] = ..., caveat_evaluation_info: _Optional[_Union[CaveatEvalInfo, _Mapping]] = ..., duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., was_cached_result: bool = ..., sub_problems: _Optional[_Union[CheckDebugTrace.SubProblems, _Mapping]] = ...) -> None: ...

class CaveatEvalInfo(_message.Message):
    __slots__ = ("expression", "result", "context", "partial_caveat_info", "caveat_name")
    class Result(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        RESULT_UNSPECIFIED: _ClassVar[CaveatEvalInfo.Result]
        RESULT_UNEVALUATED: _ClassVar[CaveatEvalInfo.Result]
        RESULT_FALSE: _ClassVar[CaveatEvalInfo.Result]
        RESULT_TRUE: _ClassVar[CaveatEvalInfo.Result]
        RESULT_MISSING_SOME_CONTEXT: _ClassVar[CaveatEvalInfo.Result]
    RESULT_UNSPECIFIED: CaveatEvalInfo.Result
    RESULT_UNEVALUATED: CaveatEvalInfo.Result
    RESULT_FALSE: CaveatEvalInfo.Result
    RESULT_TRUE: CaveatEvalInfo.Result
    RESULT_MISSING_SOME_CONTEXT: CaveatEvalInfo.Result
    EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_CAVEAT_INFO_FIELD_NUMBER: _ClassVar[int]
    CAVEAT_NAME_FIELD_NUMBER: _ClassVar[int]
    expression: str
    result: CaveatEvalInfo.Result
    context: _struct_pb2.Struct
    partial_caveat_info: _core_pb2.PartialCaveatInfo
    caveat_name: str
    def __init__(self, expression: _Optional[str] = ..., result: _Optional[_Union[CaveatEvalInfo.Result, str]] = ..., context: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., partial_caveat_info: _Optional[_Union[_core_pb2.PartialCaveatInfo, _Mapping]] = ..., caveat_name: _Optional[str] = ...) -> None: ...
