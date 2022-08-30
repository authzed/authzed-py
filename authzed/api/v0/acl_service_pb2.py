# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: authzed/api/v0/acl_service.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from validate import validate_pb2 as validate_dot_validate__pb2
from authzed.api.v0 import core_pb2 as authzed_dot_api_dot_v0_dot_core__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n authzed/api/v0/acl_service.proto\x12\x0e\x61uthzed.api.v0\x1a\x17validate/validate.proto\x1a\x19\x61uthzed/api/v0/core.proto\"\xeb\x03\n\x13RelationTupleFilter\x12\x66\n\tnamespace\x18\x01 \x01(\tBH\xfa\x42\x45rC(\x80\x01\x32>^([a-z][a-z0-9_]{1,61}[a-z0-9]/)?[a-z][a-z0-9_]{1,62}[a-z0-9]$R\tnamespace\x12M\n\tobject_id\x18\x02 \x01(\tB0\xfa\x42-r+(\x80\x01\x32&^([a-zA-Z0-9_][a-zA-Z0-9/_-]{0,127})?$R\x08objectId\x12\x46\n\x08relation\x18\x03 \x01(\tB*\xfa\x42\'r%(@2!^([a-z][a-z0-9_]{1,62}[a-z0-9])?$R\x08relation\x12;\n\x07userset\x18\x05 \x01(\x0b\x32!.authzed.api.v0.ObjectAndRelationR\x07userset\x12S\n\x07\x66ilters\x18\x06 \x03(\x0e\x32*.authzed.api.v0.RelationTupleFilter.FilterB\r\xfa\x42\n\x92\x01\x07\"\x05\x82\x01\x02\x10\x01R\x07\x66ilters\"?\n\x06\x46ilter\x12\x0b\n\x07UNKNOWN\x10\x00\x12\r\n\tOBJECT_ID\x10\x01\x12\x0c\n\x08RELATION\x10\x02\x12\x0b\n\x07USERSET\x10\x04:\x02\x18\x01\"\x9e\x01\n\x0bReadRequest\x12R\n\ttuplesets\x18\x01 \x03(\x0b\x32#.authzed.api.v0.RelationTupleFilterB\x0f\xfa\x42\x0c\x92\x01\t\x08\x01\"\x05\x8a\x01\x02\x10\x01R\ttuplesets\x12\x37\n\x0b\x61t_revision\x18\x02 \x01(\x0b\x32\x16.authzed.api.v0.ZookieR\natRevision:\x02\x18\x01\"\xce\x01\n\x0cReadResponse\x12\x43\n\ttuplesets\x18\x01 \x03(\x0b\x32%.authzed.api.v0.ReadResponse.TuplesetR\ttuplesets\x12\x32\n\x08revision\x18\x02 \x01(\x0b\x32\x16.authzed.api.v0.ZookieR\x08revision\x1a\x41\n\x08Tupleset\x12\x35\n\x06tuples\x18\x01 \x03(\x0b\x32\x1d.authzed.api.v0.RelationTupleR\x06tuples:\x02\x18\x01\"\xb9\x01\n\x0cWriteRequest\x12W\n\x10write_conditions\x18\x01 \x03(\x0b\x32\x1d.authzed.api.v0.RelationTupleB\r\xfa\x42\n\x92\x01\x07\"\x05\x8a\x01\x02\x10\x01R\x0fwriteConditions\x12L\n\x07updates\x18\x02 \x03(\x0b\x32#.authzed.api.v0.RelationTupleUpdateB\r\xfa\x42\n\x92\x01\x07\"\x05\x8a\x01\x02\x10\x01R\x07updates:\x02\x18\x01\"G\n\rWriteResponse\x12\x32\n\x08revision\x18\x01 \x01(\x0b\x32\x16.authzed.api.v0.ZookieR\x08revision:\x02\x18\x01\"\xcf\x01\n\x0c\x43heckRequest\x12N\n\x0ctest_userset\x18\x01 \x01(\x0b\x32!.authzed.api.v0.ObjectAndRelationB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01R\x0btestUserset\x12\x32\n\x04user\x18\x02 \x01(\x0b\x32\x14.authzed.api.v0.UserB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01R\x04user\x12\x37\n\x0b\x61t_revision\x18\x03 \x01(\x0b\x32\x16.authzed.api.v0.ZookieR\natRevision:\x02\x18\x01\"\xa3\x01\n\x19\x43ontentChangeCheckRequest\x12N\n\x0ctest_userset\x18\x01 \x01(\x0b\x32!.authzed.api.v0.ObjectAndRelationB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01R\x0btestUserset\x12\x32\n\x04user\x18\x02 \x01(\x0b\x32\x14.authzed.api.v0.UserB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01R\x04user:\x02\x18\x01\"\xe5\x01\n\rCheckResponse\x12\x1b\n\tis_member\x18\x01 \x01(\x08R\x08isMember\x12\x32\n\x08revision\x18\x02 \x01(\x0b\x32\x16.authzed.api.v0.ZookieR\x08revision\x12H\n\nmembership\x18\x03 \x01(\x0e\x32(.authzed.api.v0.CheckResponse.MembershipR\nmembership\"5\n\nMembership\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0e\n\nNOT_MEMBER\x10\x01\x12\n\n\x06MEMBER\x10\x02:\x02\x18\x01\"\x93\x01\n\rExpandRequest\x12\x45\n\x07userset\x18\x01 \x01(\x0b\x32!.authzed.api.v0.ObjectAndRelationB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01R\x07userset\x12\x37\n\x0b\x61t_revision\x18\x02 \x01(\x0b\x32\x16.authzed.api.v0.ZookieR\natRevision:\x02\x18\x01\"\x8c\x01\n\x0e\x45xpandResponse\x12\x42\n\ttree_node\x18\x01 \x01(\x0b\x32%.authzed.api.v0.RelationTupleTreeNodeR\x08treeNode\x12\x32\n\x08revision\x18\x03 \x01(\x0b\x32\x16.authzed.api.v0.ZookieR\x08revision:\x02\x18\x01\"\xa0\x02\n\rLookupRequest\x12T\n\x0fobject_relation\x18\x01 \x01(\x0b\x32!.authzed.api.v0.RelationReferenceB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01R\x0eobjectRelation\x12?\n\x04user\x18\x02 \x01(\x0b\x32!.authzed.api.v0.ObjectAndRelationB\x08\xfa\x42\x05\x8a\x01\x02\x10\x01R\x04user\x12\x37\n\x0b\x61t_revision\x18\x03 \x01(\x0b\x32\x16.authzed.api.v0.ZookieR\natRevision\x12%\n\x0epage_reference\x18\x04 \x01(\tR\rpageReference\x12\x14\n\x05limit\x18\x05 \x01(\rR\x05limit:\x02\x18\x01\"\xa8\x01\n\x0eLookupResponse\x12.\n\x13resolved_object_ids\x18\x01 \x03(\tR\x11resolvedObjectIds\x12.\n\x13next_page_reference\x18\x02 \x01(\tR\x11nextPageReference\x12\x32\n\x08revision\x18\x03 \x01(\x0b\x32\x16.authzed.api.v0.ZookieR\x08revision:\x02\x18\x01\x32\xeb\x03\n\nACLService\x12\x46\n\x04Read\x12\x1b.authzed.api.v0.ReadRequest\x1a\x1c.authzed.api.v0.ReadResponse\"\x03\x88\x02\x01\x12I\n\x05Write\x12\x1c.authzed.api.v0.WriteRequest\x1a\x1d.authzed.api.v0.WriteResponse\"\x03\x88\x02\x01\x12I\n\x05\x43heck\x12\x1c.authzed.api.v0.CheckRequest\x1a\x1d.authzed.api.v0.CheckResponse\"\x03\x88\x02\x01\x12\x63\n\x12\x43ontentChangeCheck\x12).authzed.api.v0.ContentChangeCheckRequest\x1a\x1d.authzed.api.v0.CheckResponse\"\x03\x88\x02\x01\x12L\n\x06\x45xpand\x12\x1d.authzed.api.v0.ExpandRequest\x1a\x1e.authzed.api.v0.ExpandResponse\"\x03\x88\x02\x01\x12L\n\x06Lookup\x12\x1d.authzed.api.v0.LookupRequest\x1a\x1e.authzed.api.v0.LookupResponse\"\x03\x88\x02\x01\x42K\n\x12\x63om.authzed.api.v0Z2github.com/authzed/authzed-go/proto/authzed/api/v0\xb8\x01\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'authzed.api.v0.acl_service_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\022com.authzed.api.v0Z2github.com/authzed/authzed-go/proto/authzed/api/v0\270\001\001'
  _RELATIONTUPLEFILTER.fields_by_name['namespace']._options = None
  _RELATIONTUPLEFILTER.fields_by_name['namespace']._serialized_options = b'\372BErC(\200\0012>^([a-z][a-z0-9_]{1,61}[a-z0-9]/)?[a-z][a-z0-9_]{1,62}[a-z0-9]$'
  _RELATIONTUPLEFILTER.fields_by_name['object_id']._options = None
  _RELATIONTUPLEFILTER.fields_by_name['object_id']._serialized_options = b'\372B-r+(\200\0012&^([a-zA-Z0-9_][a-zA-Z0-9/_-]{0,127})?$'
  _RELATIONTUPLEFILTER.fields_by_name['relation']._options = None
  _RELATIONTUPLEFILTER.fields_by_name['relation']._serialized_options = b'\372B\'r%(@2!^([a-z][a-z0-9_]{1,62}[a-z0-9])?$'
  _RELATIONTUPLEFILTER.fields_by_name['filters']._options = None
  _RELATIONTUPLEFILTER.fields_by_name['filters']._serialized_options = b'\372B\n\222\001\007\"\005\202\001\002\020\001'
  _RELATIONTUPLEFILTER._options = None
  _RELATIONTUPLEFILTER._serialized_options = b'\030\001'
  _READREQUEST.fields_by_name['tuplesets']._options = None
  _READREQUEST.fields_by_name['tuplesets']._serialized_options = b'\372B\014\222\001\t\010\001\"\005\212\001\002\020\001'
  _READREQUEST._options = None
  _READREQUEST._serialized_options = b'\030\001'
  _READRESPONSE._options = None
  _READRESPONSE._serialized_options = b'\030\001'
  _WRITEREQUEST.fields_by_name['write_conditions']._options = None
  _WRITEREQUEST.fields_by_name['write_conditions']._serialized_options = b'\372B\n\222\001\007\"\005\212\001\002\020\001'
  _WRITEREQUEST.fields_by_name['updates']._options = None
  _WRITEREQUEST.fields_by_name['updates']._serialized_options = b'\372B\n\222\001\007\"\005\212\001\002\020\001'
  _WRITEREQUEST._options = None
  _WRITEREQUEST._serialized_options = b'\030\001'
  _WRITERESPONSE._options = None
  _WRITERESPONSE._serialized_options = b'\030\001'
  _CHECKREQUEST.fields_by_name['test_userset']._options = None
  _CHECKREQUEST.fields_by_name['test_userset']._serialized_options = b'\372B\005\212\001\002\020\001'
  _CHECKREQUEST.fields_by_name['user']._options = None
  _CHECKREQUEST.fields_by_name['user']._serialized_options = b'\372B\005\212\001\002\020\001'
  _CHECKREQUEST._options = None
  _CHECKREQUEST._serialized_options = b'\030\001'
  _CONTENTCHANGECHECKREQUEST.fields_by_name['test_userset']._options = None
  _CONTENTCHANGECHECKREQUEST.fields_by_name['test_userset']._serialized_options = b'\372B\005\212\001\002\020\001'
  _CONTENTCHANGECHECKREQUEST.fields_by_name['user']._options = None
  _CONTENTCHANGECHECKREQUEST.fields_by_name['user']._serialized_options = b'\372B\005\212\001\002\020\001'
  _CONTENTCHANGECHECKREQUEST._options = None
  _CONTENTCHANGECHECKREQUEST._serialized_options = b'\030\001'
  _CHECKRESPONSE._options = None
  _CHECKRESPONSE._serialized_options = b'\030\001'
  _EXPANDREQUEST.fields_by_name['userset']._options = None
  _EXPANDREQUEST.fields_by_name['userset']._serialized_options = b'\372B\005\212\001\002\020\001'
  _EXPANDREQUEST._options = None
  _EXPANDREQUEST._serialized_options = b'\030\001'
  _EXPANDRESPONSE._options = None
  _EXPANDRESPONSE._serialized_options = b'\030\001'
  _LOOKUPREQUEST.fields_by_name['object_relation']._options = None
  _LOOKUPREQUEST.fields_by_name['object_relation']._serialized_options = b'\372B\005\212\001\002\020\001'
  _LOOKUPREQUEST.fields_by_name['user']._options = None
  _LOOKUPREQUEST.fields_by_name['user']._serialized_options = b'\372B\005\212\001\002\020\001'
  _LOOKUPREQUEST._options = None
  _LOOKUPREQUEST._serialized_options = b'\030\001'
  _LOOKUPRESPONSE._options = None
  _LOOKUPRESPONSE._serialized_options = b'\030\001'
  _ACLSERVICE.methods_by_name['Read']._options = None
  _ACLSERVICE.methods_by_name['Read']._serialized_options = b'\210\002\001'
  _ACLSERVICE.methods_by_name['Write']._options = None
  _ACLSERVICE.methods_by_name['Write']._serialized_options = b'\210\002\001'
  _ACLSERVICE.methods_by_name['Check']._options = None
  _ACLSERVICE.methods_by_name['Check']._serialized_options = b'\210\002\001'
  _ACLSERVICE.methods_by_name['ContentChangeCheck']._options = None
  _ACLSERVICE.methods_by_name['ContentChangeCheck']._serialized_options = b'\210\002\001'
  _ACLSERVICE.methods_by_name['Expand']._options = None
  _ACLSERVICE.methods_by_name['Expand']._serialized_options = b'\210\002\001'
  _ACLSERVICE.methods_by_name['Lookup']._options = None
  _ACLSERVICE.methods_by_name['Lookup']._serialized_options = b'\210\002\001'
  _RELATIONTUPLEFILTER._serialized_start=105
  _RELATIONTUPLEFILTER._serialized_end=596
  _RELATIONTUPLEFILTER_FILTER._serialized_start=529
  _RELATIONTUPLEFILTER_FILTER._serialized_end=592
  _READREQUEST._serialized_start=599
  _READREQUEST._serialized_end=757
  _READRESPONSE._serialized_start=760
  _READRESPONSE._serialized_end=966
  _READRESPONSE_TUPLESET._serialized_start=897
  _READRESPONSE_TUPLESET._serialized_end=962
  _WRITEREQUEST._serialized_start=969
  _WRITEREQUEST._serialized_end=1154
  _WRITERESPONSE._serialized_start=1156
  _WRITERESPONSE._serialized_end=1227
  _CHECKREQUEST._serialized_start=1230
  _CHECKREQUEST._serialized_end=1437
  _CONTENTCHANGECHECKREQUEST._serialized_start=1440
  _CONTENTCHANGECHECKREQUEST._serialized_end=1603
  _CHECKRESPONSE._serialized_start=1606
  _CHECKRESPONSE._serialized_end=1835
  _CHECKRESPONSE_MEMBERSHIP._serialized_start=1778
  _CHECKRESPONSE_MEMBERSHIP._serialized_end=1831
  _EXPANDREQUEST._serialized_start=1838
  _EXPANDREQUEST._serialized_end=1985
  _EXPANDRESPONSE._serialized_start=1988
  _EXPANDRESPONSE._serialized_end=2128
  _LOOKUPREQUEST._serialized_start=2131
  _LOOKUPREQUEST._serialized_end=2419
  _LOOKUPRESPONSE._serialized_start=2422
  _LOOKUPRESPONSE._serialized_end=2590
  _ACLSERVICE._serialized_start=2593
  _ACLSERVICE._serialized_end=3084
# @@protoc_insertion_point(module_scope)
