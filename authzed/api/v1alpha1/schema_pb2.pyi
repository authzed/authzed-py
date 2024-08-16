from validate import validate_pb2 as _validate_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ReadSchemaRequest(_message.Message):
    __slots__ = ("object_definitions_names",)
    OBJECT_DEFINITIONS_NAMES_FIELD_NUMBER: _ClassVar[int]
    object_definitions_names: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, object_definitions_names: _Optional[_Iterable[str]] = ...) -> None: ...

class ReadSchemaResponse(_message.Message):
    __slots__ = ("object_definitions", "computed_definitions_revision")
    OBJECT_DEFINITIONS_FIELD_NUMBER: _ClassVar[int]
    COMPUTED_DEFINITIONS_REVISION_FIELD_NUMBER: _ClassVar[int]
    object_definitions: _containers.RepeatedScalarFieldContainer[str]
    computed_definitions_revision: str
    def __init__(self, object_definitions: _Optional[_Iterable[str]] = ..., computed_definitions_revision: _Optional[str] = ...) -> None: ...

class WriteSchemaRequest(_message.Message):
    __slots__ = ("schema", "optional_definitions_revision_precondition")
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    OPTIONAL_DEFINITIONS_REVISION_PRECONDITION_FIELD_NUMBER: _ClassVar[int]
    schema: str
    optional_definitions_revision_precondition: str
    def __init__(self, schema: _Optional[str] = ..., optional_definitions_revision_precondition: _Optional[str] = ...) -> None: ...

class WriteSchemaResponse(_message.Message):
    __slots__ = ("object_definitions_names", "computed_definitions_revision")
    OBJECT_DEFINITIONS_NAMES_FIELD_NUMBER: _ClassVar[int]
    COMPUTED_DEFINITIONS_REVISION_FIELD_NUMBER: _ClassVar[int]
    object_definitions_names: _containers.RepeatedScalarFieldContainer[str]
    computed_definitions_revision: str
    def __init__(self, object_definitions_names: _Optional[_Iterable[str]] = ..., computed_definitions_revision: _Optional[str] = ...) -> None: ...
