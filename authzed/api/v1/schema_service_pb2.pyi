from google.api import annotations_pb2 as _annotations_pb2
from validate import validate_pb2 as _validate_pb2
from authzed.api.v1 import core_pb2 as _core_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ReadSchemaRequest(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class ReadSchemaResponse(_message.Message):
    __slots__ = ("schema_text", "read_at")
    SCHEMA_TEXT_FIELD_NUMBER: _ClassVar[int]
    READ_AT_FIELD_NUMBER: _ClassVar[int]
    schema_text: str
    read_at: _core_pb2.ZedToken
    def __init__(self, schema_text: _Optional[str] = ..., read_at: _Optional[_Union[_core_pb2.ZedToken, _Mapping]] = ...) -> None: ...

class WriteSchemaRequest(_message.Message):
    __slots__ = ("schema",)
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    schema: str
    def __init__(self, schema: _Optional[str] = ...) -> None: ...

class WriteSchemaResponse(_message.Message):
    __slots__ = ("written_at",)
    WRITTEN_AT_FIELD_NUMBER: _ClassVar[int]
    written_at: _core_pb2.ZedToken
    def __init__(self, written_at: _Optional[_Union[_core_pb2.ZedToken, _Mapping]] = ...) -> None: ...
