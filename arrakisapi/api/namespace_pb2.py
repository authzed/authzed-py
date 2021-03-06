# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: arrakisapi/api/namespace.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='arrakisapi/api/namespace.proto',
  package='',
  syntax='proto3',
  serialized_options=b'Z$github.com/petricorp/code/arrakisapi',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1e\x61rrakisapi/api/namespace.proto\"@\n\x13NamespaceDefinition\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x1b\n\x08relation\x18\x02 \x03(\x0b\x32\t.Relation\"B\n\x08Relation\x12\x0c\n\x04name\x18\x01 \x01(\t\x12(\n\x0fuserset_rewrite\x18\x02 \x01(\x0b\x32\x0f.UsersetRewrite\"\x90\x01\n\x0eUsersetRewrite\x12\x1e\n\x05union\x18\x01 \x01(\x0b\x32\r.SetOperationH\x00\x12%\n\x0cintersection\x18\x02 \x01(\x0b\x32\r.SetOperationH\x00\x12\"\n\texclusion\x18\x03 \x01(\x0b\x32\r.SetOperationH\x00\x42\x13\n\x11rewrite_operation\"\x84\x02\n\x0cSetOperation\x12\"\n\x05\x63hild\x18\x01 \x03(\x0b\x32\x13.SetOperation.Child\x1a\xcf\x01\n\x05\x43hild\x12)\n\x05_this\x18\x01 \x01(\x0b\x32\x18.SetOperation.Child.ThisH\x00\x12,\n\x10\x63omputed_userset\x18\x02 \x01(\x0b\x32\x10.ComputedUsersetH\x00\x12+\n\x10tuple_to_userset\x18\x03 \x01(\x0b\x32\x0f.TupleToUsersetH\x00\x12*\n\x0fuserset_rewrite\x18\x04 \x01(\x0b\x32\x0f.UsersetRewriteH\x00\x1a\x06\n\x04ThisB\x0c\n\nchild_type\"\x86\x01\n\x0eTupleToUserset\x12*\n\x08tupleset\x18\x01 \x01(\x0b\x32\x18.TupleToUserset.Tupleset\x12*\n\x10\x63omputed_userset\x18\x02 \x01(\x0b\x32\x10.ComputedUserset\x1a\x1c\n\x08Tupleset\x12\x10\n\x08relation\x18\x01 \x01(\t\"\x82\x01\n\x0f\x43omputedUserset\x12\'\n\x06object\x18\x01 \x01(\x0e\x32\x17.ComputedUserset.Object\x12\x10\n\x08relation\x18\x02 \x01(\t\"4\n\x06Object\x12\x10\n\x0cTUPLE_OBJECT\x10\x00\x12\x18\n\x14TUPLE_USERSET_OBJECT\x10\x01\x42&Z$github.com/petricorp/code/arrakisapib\x06proto3'
)



_COMPUTEDUSERSET_OBJECT = _descriptor.EnumDescriptor(
  name='Object',
  full_name='ComputedUserset.Object',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TUPLE_OBJECT', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TUPLE_USERSET_OBJECT', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=794,
  serialized_end=846,
)
_sym_db.RegisterEnumDescriptor(_COMPUTEDUSERSET_OBJECT)


_NAMESPACEDEFINITION = _descriptor.Descriptor(
  name='NamespaceDefinition',
  full_name='NamespaceDefinition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='NamespaceDefinition.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='relation', full_name='NamespaceDefinition.relation', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=34,
  serialized_end=98,
)


_RELATION = _descriptor.Descriptor(
  name='Relation',
  full_name='Relation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Relation.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='userset_rewrite', full_name='Relation.userset_rewrite', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=100,
  serialized_end=166,
)


_USERSETREWRITE = _descriptor.Descriptor(
  name='UsersetRewrite',
  full_name='UsersetRewrite',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='union', full_name='UsersetRewrite.union', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='intersection', full_name='UsersetRewrite.intersection', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='exclusion', full_name='UsersetRewrite.exclusion', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='rewrite_operation', full_name='UsersetRewrite.rewrite_operation',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=169,
  serialized_end=313,
)


_SETOPERATION_CHILD_THIS = _descriptor.Descriptor(
  name='This',
  full_name='SetOperation.Child.This',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=556,
  serialized_end=562,
)

_SETOPERATION_CHILD = _descriptor.Descriptor(
  name='Child',
  full_name='SetOperation.Child',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='_this', full_name='SetOperation.Child._this', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='computed_userset', full_name='SetOperation.Child.computed_userset', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tuple_to_userset', full_name='SetOperation.Child.tuple_to_userset', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='userset_rewrite', full_name='SetOperation.Child.userset_rewrite', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_SETOPERATION_CHILD_THIS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='child_type', full_name='SetOperation.Child.child_type',
      index=0, containing_type=None,
      create_key=_descriptor._internal_create_key,
    fields=[]),
  ],
  serialized_start=369,
  serialized_end=576,
)

_SETOPERATION = _descriptor.Descriptor(
  name='SetOperation',
  full_name='SetOperation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='child', full_name='SetOperation.child', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_SETOPERATION_CHILD, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=316,
  serialized_end=576,
)


_TUPLETOUSERSET_TUPLESET = _descriptor.Descriptor(
  name='Tupleset',
  full_name='TupleToUserset.Tupleset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='relation', full_name='TupleToUserset.Tupleset.relation', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=685,
  serialized_end=713,
)

_TUPLETOUSERSET = _descriptor.Descriptor(
  name='TupleToUserset',
  full_name='TupleToUserset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tupleset', full_name='TupleToUserset.tupleset', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='computed_userset', full_name='TupleToUserset.computed_userset', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_TUPLETOUSERSET_TUPLESET, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=579,
  serialized_end=713,
)


_COMPUTEDUSERSET = _descriptor.Descriptor(
  name='ComputedUserset',
  full_name='ComputedUserset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='object', full_name='ComputedUserset.object', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='relation', full_name='ComputedUserset.relation', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _COMPUTEDUSERSET_OBJECT,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=716,
  serialized_end=846,
)

_NAMESPACEDEFINITION.fields_by_name['relation'].message_type = _RELATION
_RELATION.fields_by_name['userset_rewrite'].message_type = _USERSETREWRITE
_USERSETREWRITE.fields_by_name['union'].message_type = _SETOPERATION
_USERSETREWRITE.fields_by_name['intersection'].message_type = _SETOPERATION
_USERSETREWRITE.fields_by_name['exclusion'].message_type = _SETOPERATION
_USERSETREWRITE.oneofs_by_name['rewrite_operation'].fields.append(
  _USERSETREWRITE.fields_by_name['union'])
_USERSETREWRITE.fields_by_name['union'].containing_oneof = _USERSETREWRITE.oneofs_by_name['rewrite_operation']
_USERSETREWRITE.oneofs_by_name['rewrite_operation'].fields.append(
  _USERSETREWRITE.fields_by_name['intersection'])
_USERSETREWRITE.fields_by_name['intersection'].containing_oneof = _USERSETREWRITE.oneofs_by_name['rewrite_operation']
_USERSETREWRITE.oneofs_by_name['rewrite_operation'].fields.append(
  _USERSETREWRITE.fields_by_name['exclusion'])
_USERSETREWRITE.fields_by_name['exclusion'].containing_oneof = _USERSETREWRITE.oneofs_by_name['rewrite_operation']
_SETOPERATION_CHILD_THIS.containing_type = _SETOPERATION_CHILD
_SETOPERATION_CHILD.fields_by_name['_this'].message_type = _SETOPERATION_CHILD_THIS
_SETOPERATION_CHILD.fields_by_name['computed_userset'].message_type = _COMPUTEDUSERSET
_SETOPERATION_CHILD.fields_by_name['tuple_to_userset'].message_type = _TUPLETOUSERSET
_SETOPERATION_CHILD.fields_by_name['userset_rewrite'].message_type = _USERSETREWRITE
_SETOPERATION_CHILD.containing_type = _SETOPERATION
_SETOPERATION_CHILD.oneofs_by_name['child_type'].fields.append(
  _SETOPERATION_CHILD.fields_by_name['_this'])
_SETOPERATION_CHILD.fields_by_name['_this'].containing_oneof = _SETOPERATION_CHILD.oneofs_by_name['child_type']
_SETOPERATION_CHILD.oneofs_by_name['child_type'].fields.append(
  _SETOPERATION_CHILD.fields_by_name['computed_userset'])
_SETOPERATION_CHILD.fields_by_name['computed_userset'].containing_oneof = _SETOPERATION_CHILD.oneofs_by_name['child_type']
_SETOPERATION_CHILD.oneofs_by_name['child_type'].fields.append(
  _SETOPERATION_CHILD.fields_by_name['tuple_to_userset'])
_SETOPERATION_CHILD.fields_by_name['tuple_to_userset'].containing_oneof = _SETOPERATION_CHILD.oneofs_by_name['child_type']
_SETOPERATION_CHILD.oneofs_by_name['child_type'].fields.append(
  _SETOPERATION_CHILD.fields_by_name['userset_rewrite'])
_SETOPERATION_CHILD.fields_by_name['userset_rewrite'].containing_oneof = _SETOPERATION_CHILD.oneofs_by_name['child_type']
_SETOPERATION.fields_by_name['child'].message_type = _SETOPERATION_CHILD
_TUPLETOUSERSET_TUPLESET.containing_type = _TUPLETOUSERSET
_TUPLETOUSERSET.fields_by_name['tupleset'].message_type = _TUPLETOUSERSET_TUPLESET
_TUPLETOUSERSET.fields_by_name['computed_userset'].message_type = _COMPUTEDUSERSET
_COMPUTEDUSERSET.fields_by_name['object'].enum_type = _COMPUTEDUSERSET_OBJECT
_COMPUTEDUSERSET_OBJECT.containing_type = _COMPUTEDUSERSET
DESCRIPTOR.message_types_by_name['NamespaceDefinition'] = _NAMESPACEDEFINITION
DESCRIPTOR.message_types_by_name['Relation'] = _RELATION
DESCRIPTOR.message_types_by_name['UsersetRewrite'] = _USERSETREWRITE
DESCRIPTOR.message_types_by_name['SetOperation'] = _SETOPERATION
DESCRIPTOR.message_types_by_name['TupleToUserset'] = _TUPLETOUSERSET
DESCRIPTOR.message_types_by_name['ComputedUserset'] = _COMPUTEDUSERSET
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NamespaceDefinition = _reflection.GeneratedProtocolMessageType('NamespaceDefinition', (_message.Message,), {
  'DESCRIPTOR' : _NAMESPACEDEFINITION,
  '__module__' : 'arrakisapi.api.namespace_pb2'
  # @@protoc_insertion_point(class_scope:NamespaceDefinition)
  })
_sym_db.RegisterMessage(NamespaceDefinition)

Relation = _reflection.GeneratedProtocolMessageType('Relation', (_message.Message,), {
  'DESCRIPTOR' : _RELATION,
  '__module__' : 'arrakisapi.api.namespace_pb2'
  # @@protoc_insertion_point(class_scope:Relation)
  })
_sym_db.RegisterMessage(Relation)

UsersetRewrite = _reflection.GeneratedProtocolMessageType('UsersetRewrite', (_message.Message,), {
  'DESCRIPTOR' : _USERSETREWRITE,
  '__module__' : 'arrakisapi.api.namespace_pb2'
  # @@protoc_insertion_point(class_scope:UsersetRewrite)
  })
_sym_db.RegisterMessage(UsersetRewrite)

SetOperation = _reflection.GeneratedProtocolMessageType('SetOperation', (_message.Message,), {

  'Child' : _reflection.GeneratedProtocolMessageType('Child', (_message.Message,), {

    'This' : _reflection.GeneratedProtocolMessageType('This', (_message.Message,), {
      'DESCRIPTOR' : _SETOPERATION_CHILD_THIS,
      '__module__' : 'arrakisapi.api.namespace_pb2'
      # @@protoc_insertion_point(class_scope:SetOperation.Child.This)
      })
    ,
    'DESCRIPTOR' : _SETOPERATION_CHILD,
    '__module__' : 'arrakisapi.api.namespace_pb2'
    # @@protoc_insertion_point(class_scope:SetOperation.Child)
    })
  ,
  'DESCRIPTOR' : _SETOPERATION,
  '__module__' : 'arrakisapi.api.namespace_pb2'
  # @@protoc_insertion_point(class_scope:SetOperation)
  })
_sym_db.RegisterMessage(SetOperation)
_sym_db.RegisterMessage(SetOperation.Child)
_sym_db.RegisterMessage(SetOperation.Child.This)

TupleToUserset = _reflection.GeneratedProtocolMessageType('TupleToUserset', (_message.Message,), {

  'Tupleset' : _reflection.GeneratedProtocolMessageType('Tupleset', (_message.Message,), {
    'DESCRIPTOR' : _TUPLETOUSERSET_TUPLESET,
    '__module__' : 'arrakisapi.api.namespace_pb2'
    # @@protoc_insertion_point(class_scope:TupleToUserset.Tupleset)
    })
  ,
  'DESCRIPTOR' : _TUPLETOUSERSET,
  '__module__' : 'arrakisapi.api.namespace_pb2'
  # @@protoc_insertion_point(class_scope:TupleToUserset)
  })
_sym_db.RegisterMessage(TupleToUserset)
_sym_db.RegisterMessage(TupleToUserset.Tupleset)

ComputedUserset = _reflection.GeneratedProtocolMessageType('ComputedUserset', (_message.Message,), {
  'DESCRIPTOR' : _COMPUTEDUSERSET,
  '__module__' : 'arrakisapi.api.namespace_pb2'
  # @@protoc_insertion_point(class_scope:ComputedUserset)
  })
_sym_db.RegisterMessage(ComputedUserset)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
