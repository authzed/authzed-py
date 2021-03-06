# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from arrakisapi.api.core_pb2 import (
    RelationTupleUpdate as arrakisapi___api___core_pb2___RelationTupleUpdate,
    Zookie as arrakisapi___api___core_pb2___Zookie,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int


DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class WatchRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    namespaces: google___protobuf___internal___containers___RepeatedScalarFieldContainer[typing___Text] = ...

    @property
    def start_revision(self) -> arrakisapi___api___core_pb2___Zookie: ...

    def __init__(self,
        *,
        namespaces : typing___Optional[typing___Iterable[typing___Text]] = None,
        start_revision : typing___Optional[arrakisapi___api___core_pb2___Zookie] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"start_revision",b"start_revision"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"namespaces",b"namespaces",u"start_revision",b"start_revision"]) -> None: ...
type___WatchRequest = WatchRequest

class WatchResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def updates(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[arrakisapi___api___core_pb2___RelationTupleUpdate]: ...

    @property
    def end_revision(self) -> arrakisapi___api___core_pb2___Zookie: ...

    def __init__(self,
        *,
        updates : typing___Optional[typing___Iterable[arrakisapi___api___core_pb2___RelationTupleUpdate]] = None,
        end_revision : typing___Optional[arrakisapi___api___core_pb2___Zookie] = None,
        ) -> None: ...
    def HasField(self, field_name: typing_extensions___Literal[u"end_revision",b"end_revision"]) -> builtin___bool: ...
    def ClearField(self, field_name: typing_extensions___Literal[u"end_revision",b"end_revision",u"updates",b"updates"]) -> None: ...
type___WatchResponse = WatchResponse
