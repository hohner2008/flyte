# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: flyteidl/admin/common.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from flyteidl.core import execution_pb2 as flyteidl_dot_core_dot_execution__pb2
from flyteidl.core import identifier_pb2 as flyteidl_dot_core_dot_identifier__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1b\x66lyteidl/admin/common.proto\x12\x0e\x66lyteidl.admin\x1a\x1d\x66lyteidl/core/execution.proto\x1a\x1e\x66lyteidl/core/identifier.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"]\n\x15NamedEntityIdentifier\x12\x18\n\x07project\x18\x01 \x01(\tR\x07project\x12\x16\n\x06\x64omain\x18\x02 \x01(\tR\x06\x64omain\x12\x12\n\x04name\x18\x03 \x01(\tR\x04name\"o\n\x13NamedEntityMetadata\x12 \n\x0b\x64\x65scription\x18\x01 \x01(\tR\x0b\x64\x65scription\x12\x36\n\x05state\x18\x02 \x01(\x0e\x32 .flyteidl.admin.NamedEntityStateR\x05state\"\xc7\x01\n\x0bNamedEntity\x12@\n\rresource_type\x18\x01 \x01(\x0e\x32\x1b.flyteidl.core.ResourceTypeR\x0cresourceType\x12\x35\n\x02id\x18\x02 \x01(\x0b\x32%.flyteidl.admin.NamedEntityIdentifierR\x02id\x12?\n\x08metadata\x18\x03 \x01(\x0b\x32#.flyteidl.admin.NamedEntityMetadataR\x08metadata\"\x82\x01\n\x04Sort\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12<\n\tdirection\x18\x02 \x01(\x0e\x32\x1e.flyteidl.admin.Sort.DirectionR\tdirection\"*\n\tDirection\x12\x0e\n\nDESCENDING\x10\x00\x12\r\n\tASCENDING\x10\x01\"\xc9\x01\n NamedEntityIdentifierListRequest\x12\x18\n\x07project\x18\x01 \x01(\tR\x07project\x12\x16\n\x06\x64omain\x18\x02 \x01(\tR\x06\x64omain\x12\x14\n\x05limit\x18\x03 \x01(\rR\x05limit\x12\x14\n\x05token\x18\x04 \x01(\tR\x05token\x12-\n\x07sort_by\x18\x05 \x01(\x0b\x32\x14.flyteidl.admin.SortR\x06sortBy\x12\x18\n\x07\x66ilters\x18\x06 \x01(\tR\x07\x66ilters\"\x81\x02\n\x16NamedEntityListRequest\x12@\n\rresource_type\x18\x01 \x01(\x0e\x32\x1b.flyteidl.core.ResourceTypeR\x0cresourceType\x12\x18\n\x07project\x18\x02 \x01(\tR\x07project\x12\x16\n\x06\x64omain\x18\x03 \x01(\tR\x06\x64omain\x12\x14\n\x05limit\x18\x04 \x01(\rR\x05limit\x12\x14\n\x05token\x18\x05 \x01(\tR\x05token\x12-\n\x07sort_by\x18\x06 \x01(\x0b\x32\x14.flyteidl.admin.SortR\x06sortBy\x12\x18\n\x07\x66ilters\x18\x07 \x01(\tR\x07\x66ilters\"t\n\x19NamedEntityIdentifierList\x12\x41\n\x08\x65ntities\x18\x01 \x03(\x0b\x32%.flyteidl.admin.NamedEntityIdentifierR\x08\x65ntities\x12\x14\n\x05token\x18\x02 \x01(\tR\x05token\"`\n\x0fNamedEntityList\x12\x37\n\x08\x65ntities\x18\x01 \x03(\x0b\x32\x1b.flyteidl.admin.NamedEntityR\x08\x65ntities\x12\x14\n\x05token\x18\x02 \x01(\tR\x05token\"\x90\x01\n\x15NamedEntityGetRequest\x12@\n\rresource_type\x18\x01 \x01(\x0e\x32\x1b.flyteidl.core.ResourceTypeR\x0cresourceType\x12\x35\n\x02id\x18\x02 \x01(\x0b\x32%.flyteidl.admin.NamedEntityIdentifierR\x02id\"\xd4\x01\n\x18NamedEntityUpdateRequest\x12@\n\rresource_type\x18\x01 \x01(\x0e\x32\x1b.flyteidl.core.ResourceTypeR\x0cresourceType\x12\x35\n\x02id\x18\x02 \x01(\x0b\x32%.flyteidl.admin.NamedEntityIdentifierR\x02id\x12?\n\x08metadata\x18\x03 \x01(\x0b\x32#.flyteidl.admin.NamedEntityMetadataR\x08metadata\"\x1b\n\x19NamedEntityUpdateResponse\"=\n\x10ObjectGetRequest\x12)\n\x02id\x18\x01 \x01(\x0b\x32\x19.flyteidl.core.IdentifierR\x02id\"\xc1\x01\n\x13ResourceListRequest\x12\x35\n\x02id\x18\x01 \x01(\x0b\x32%.flyteidl.admin.NamedEntityIdentifierR\x02id\x12\x14\n\x05limit\x18\x02 \x01(\rR\x05limit\x12\x14\n\x05token\x18\x03 \x01(\tR\x05token\x12\x18\n\x07\x66ilters\x18\x04 \x01(\tR\x07\x66ilters\x12-\n\x07sort_by\x18\x05 \x01(\x0b\x32\x14.flyteidl.admin.SortR\x06sortBy\">\n\x11\x45mailNotification\x12)\n\x10recipients_email\x18\x01 \x03(\tR\x0frecipientsEmail\"B\n\x15PagerDutyNotification\x12)\n\x10recipients_email\x18\x01 \x03(\tR\x0frecipientsEmail\">\n\x11SlackNotification\x12)\n\x10recipients_email\x18\x01 \x03(\tR\x0frecipientsEmail\"\x94\x02\n\x0cNotification\x12>\n\x06phases\x18\x01 \x03(\x0e\x32&.flyteidl.core.WorkflowExecution.PhaseR\x06phases\x12\x39\n\x05\x65mail\x18\x02 \x01(\x0b\x32!.flyteidl.admin.EmailNotificationH\x00R\x05\x65mail\x12\x46\n\npager_duty\x18\x03 \x01(\x0b\x32%.flyteidl.admin.PagerDutyNotificationH\x00R\tpagerDuty\x12\x39\n\x05slack\x18\x04 \x01(\x0b\x32!.flyteidl.admin.SlackNotificationH\x00R\x05slackB\x06\n\x04type\"5\n\x07UrlBlob\x12\x10\n\x03url\x18\x01 \x01(\tR\x03url\x12\x14\n\x05\x62ytes\x18\x02 \x01(\x03R\x05\x62ytes:\x02\x18\x01\"\x7f\n\x06Labels\x12:\n\x06values\x18\x01 \x03(\x0b\x32\".flyteidl.admin.Labels.ValuesEntryR\x06values\x1a\x39\n\x0bValuesEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"\x89\x01\n\x0b\x41nnotations\x12?\n\x06values\x18\x01 \x03(\x0b\x32\'.flyteidl.admin.Annotations.ValuesEntryR\x06values\x1a\x39\n\x0bValuesEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"z\n\x08\x41uthRole\x12,\n\x12\x61ssumable_iam_role\x18\x01 \x01(\tR\x10\x61ssumableIamRole\x12<\n\x1akubernetes_service_account\x18\x02 \x01(\tR\x18kubernetesServiceAccount:\x02\x18\x01\"K\n\x13RawOutputDataConfig\x12\x34\n\x16output_location_prefix\x18\x01 \x01(\tR\x14outputLocationPrefix\"Q\n\tFlyteURLs\x12\x16\n\x06inputs\x18\x01 \x01(\tR\x06inputs\x12\x18\n\x07outputs\x18\x02 \x01(\tR\x07outputs\x12\x12\n\x04\x64\x65\x63k\x18\x03 \x01(\tR\x04\x64\x65\x63k*\\\n\x10NamedEntityState\x12\x17\n\x13NAMED_ENTITY_ACTIVE\x10\x00\x12\x19\n\x15NAMED_ENTITY_ARCHIVED\x10\x01\x12\x14\n\x10SYSTEM_GENERATED\x10\x02\x42\xb1\x01\n\x12\x63om.flyteidl.adminB\x0b\x43ommonProtoP\x01Z5github.com/flyteorg/flyteidl/gen/pb-go/flyteidl/admin\xa2\x02\x03\x46\x41X\xaa\x02\x0e\x46lyteidl.Admin\xca\x02\x0e\x46lyteidl\\Admin\xe2\x02\x1a\x46lyteidl\\Admin\\GPBMetadata\xea\x02\x0f\x46lyteidl::Adminb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'flyteidl.admin.common_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\022com.flyteidl.adminB\013CommonProtoP\001Z5github.com/flyteorg/flyteidl/gen/pb-go/flyteidl/admin\242\002\003FAX\252\002\016Flyteidl.Admin\312\002\016Flyteidl\\Admin\342\002\032Flyteidl\\Admin\\GPBMetadata\352\002\017Flyteidl::Admin'
  _URLBLOB._options = None
  _URLBLOB._serialized_options = b'\030\001'
  _LABELS_VALUESENTRY._options = None
  _LABELS_VALUESENTRY._serialized_options = b'8\001'
  _ANNOTATIONS_VALUESENTRY._options = None
  _ANNOTATIONS_VALUESENTRY._serialized_options = b'8\001'
  _AUTHROLE._options = None
  _AUTHROLE._serialized_options = b'\030\001'
  _globals['_NAMEDENTITYSTATE']._serialized_start=3099
  _globals['_NAMEDENTITYSTATE']._serialized_end=3191
  _globals['_NAMEDENTITYIDENTIFIER']._serialized_start=143
  _globals['_NAMEDENTITYIDENTIFIER']._serialized_end=236
  _globals['_NAMEDENTITYMETADATA']._serialized_start=238
  _globals['_NAMEDENTITYMETADATA']._serialized_end=349
  _globals['_NAMEDENTITY']._serialized_start=352
  _globals['_NAMEDENTITY']._serialized_end=551
  _globals['_SORT']._serialized_start=554
  _globals['_SORT']._serialized_end=684
  _globals['_SORT_DIRECTION']._serialized_start=642
  _globals['_SORT_DIRECTION']._serialized_end=684
  _globals['_NAMEDENTITYIDENTIFIERLISTREQUEST']._serialized_start=687
  _globals['_NAMEDENTITYIDENTIFIERLISTREQUEST']._serialized_end=888
  _globals['_NAMEDENTITYLISTREQUEST']._serialized_start=891
  _globals['_NAMEDENTITYLISTREQUEST']._serialized_end=1148
  _globals['_NAMEDENTITYIDENTIFIERLIST']._serialized_start=1150
  _globals['_NAMEDENTITYIDENTIFIERLIST']._serialized_end=1266
  _globals['_NAMEDENTITYLIST']._serialized_start=1268
  _globals['_NAMEDENTITYLIST']._serialized_end=1364
  _globals['_NAMEDENTITYGETREQUEST']._serialized_start=1367
  _globals['_NAMEDENTITYGETREQUEST']._serialized_end=1511
  _globals['_NAMEDENTITYUPDATEREQUEST']._serialized_start=1514
  _globals['_NAMEDENTITYUPDATEREQUEST']._serialized_end=1726
  _globals['_NAMEDENTITYUPDATERESPONSE']._serialized_start=1728
  _globals['_NAMEDENTITYUPDATERESPONSE']._serialized_end=1755
  _globals['_OBJECTGETREQUEST']._serialized_start=1757
  _globals['_OBJECTGETREQUEST']._serialized_end=1818
  _globals['_RESOURCELISTREQUEST']._serialized_start=1821
  _globals['_RESOURCELISTREQUEST']._serialized_end=2014
  _globals['_EMAILNOTIFICATION']._serialized_start=2016
  _globals['_EMAILNOTIFICATION']._serialized_end=2078
  _globals['_PAGERDUTYNOTIFICATION']._serialized_start=2080
  _globals['_PAGERDUTYNOTIFICATION']._serialized_end=2146
  _globals['_SLACKNOTIFICATION']._serialized_start=2148
  _globals['_SLACKNOTIFICATION']._serialized_end=2210
  _globals['_NOTIFICATION']._serialized_start=2213
  _globals['_NOTIFICATION']._serialized_end=2489
  _globals['_URLBLOB']._serialized_start=2491
  _globals['_URLBLOB']._serialized_end=2544
  _globals['_LABELS']._serialized_start=2546
  _globals['_LABELS']._serialized_end=2673
  _globals['_LABELS_VALUESENTRY']._serialized_start=2616
  _globals['_LABELS_VALUESENTRY']._serialized_end=2673
  _globals['_ANNOTATIONS']._serialized_start=2676
  _globals['_ANNOTATIONS']._serialized_end=2813
  _globals['_ANNOTATIONS_VALUESENTRY']._serialized_start=2616
  _globals['_ANNOTATIONS_VALUESENTRY']._serialized_end=2673
  _globals['_AUTHROLE']._serialized_start=2815
  _globals['_AUTHROLE']._serialized_end=2937
  _globals['_RAWOUTPUTDATACONFIG']._serialized_start=2939
  _globals['_RAWOUTPUTDATACONFIG']._serialized_end=3014
  _globals['_FLYTEURLS']._serialized_start=3016
  _globals['_FLYTEURLS']._serialized_end=3097
# @@protoc_insertion_point(module_scope)
