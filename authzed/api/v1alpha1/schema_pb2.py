# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: authzed/api/v1alpha1/schema.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!authzed/api/v1alpha1/schema.proto\x12\x14\x61uthzed.api.v1alpha1\x1a\x17validate/validate.proto\"\x9d\x01\n\x11ReadSchemaRequest\x12\x87\x01\n\x18object_definitions_names\x18\x01 \x03(\tBM\xfa\x42J\x92\x01G\"ErC(\x80\x01\x32>^([a-z][a-z0-9_]{1,62}[a-z0-9]/)*[a-z][a-z0-9_]{1,62}[a-z0-9]$R\x16objectDefinitionsNames\"\x87\x01\n\x12ReadSchemaResponse\x12-\n\x12object_definitions\x18\x01 \x03(\tR\x11objectDefinitions\x12\x42\n\x1d\x63omputed_definitions_revision\x18\x02 \x01(\tR\x1b\x63omputedDefinitionsRevision\"\x94\x01\n\x12WriteSchemaRequest\x12!\n\x06schema\x18\x01 \x01(\tB\t\xfa\x42\x06r\x04(\x80\x80\x10R\x06schema\x12[\n*optional_definitions_revision_precondition\x18\x02 \x01(\tR\'optionalDefinitionsRevisionPrecondition\"\x93\x01\n\x13WriteSchemaResponse\x12\x38\n\x18object_definitions_names\x18\x01 \x03(\tR\x16objectDefinitionsNames\x12\x42\n\x1d\x63omputed_definitions_revision\x18\x02 \x01(\tR\x1b\x63omputedDefinitionsRevision2\xd8\x01\n\rSchemaService\x12\x61\n\nReadSchema\x12\'.authzed.api.v1alpha1.ReadSchemaRequest\x1a(.authzed.api.v1alpha1.ReadSchemaResponse\"\x00\x12\x64\n\x0bWriteSchema\x12(.authzed.api.v1alpha1.WriteSchemaRequest\x1a).authzed.api.v1alpha1.WriteSchemaResponse\"\x00\x42T\n\x18\x63om.authzed.api.v1alpha1Z8github.com/authzed/authzed-go/proto/authzed/api/v1alpha1b\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'authzed.api.v1alpha1.schema_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\030com.authzed.api.v1alpha1Z8github.com/authzed/authzed-go/proto/authzed/api/v1alpha1'
  _READSCHEMAREQUEST.fields_by_name['object_definitions_names']._options = None
  _READSCHEMAREQUEST.fields_by_name['object_definitions_names']._serialized_options = b'\372BJ\222\001G\"ErC(\200\0012>^([a-z][a-z0-9_]{1,62}[a-z0-9]/)*[a-z][a-z0-9_]{1,62}[a-z0-9]$'
  _WRITESCHEMAREQUEST.fields_by_name['schema']._options = None
  _WRITESCHEMAREQUEST.fields_by_name['schema']._serialized_options = b'\372B\006r\004(\200\200\020'
  _globals['_READSCHEMAREQUEST']._serialized_start=85
  _globals['_READSCHEMAREQUEST']._serialized_end=242
  _globals['_READSCHEMARESPONSE']._serialized_start=245
  _globals['_READSCHEMARESPONSE']._serialized_end=380
  _globals['_WRITESCHEMAREQUEST']._serialized_start=383
  _globals['_WRITESCHEMAREQUEST']._serialized_end=531
  _globals['_WRITESCHEMARESPONSE']._serialized_start=534
  _globals['_WRITESCHEMARESPONSE']._serialized_end=681
  _globals['_SCHEMASERVICE']._serialized_start=684
  _globals['_SCHEMASERVICE']._serialized_end=900
# @@protoc_insertion_point(module_scope)
