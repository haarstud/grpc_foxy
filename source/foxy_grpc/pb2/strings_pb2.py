# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: foxy_grpc/pb2/strings.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'foxy_grpc/pb2/strings.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1b\x66oxy_grpc/pb2/strings.proto\"A\n\rStringRequest\x12\r\n\x05\x63ount\x18\x01 \x01(\r\x12\x0f\n\x07\x66orever\x18\x02 \x01(\x08\x12\x10\n\x08interval\x18\x03 \x01(\x02\"!\n\x0eStringResponse\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\t\"\x0e\n\x0c\x45mptyMessage\"\x17\n\x06Number\x12\r\n\x05value\x18\x01 \x01(\x02\"4\n\x07WhatAmI\x12\x0e\n\x04text\x18\x01 \x01(\tH\x00\x12\x10\n\x06number\x18\x02 \x01(\x02H\x00\x42\x07\n\x05value2\xb0\x01\n\rStringService\x12\x31\n\nGetStrings\x12\x0e.StringRequest\x1a\x0f.StringResponse\"\x00\x30\x01\x12\'\n\x05SayHi\x12\r.EmptyMessage\x1a\r.EmptyMessage\"\x00\x12\x1c\n\x06Square\x12\x07.Number\x1a\x07.Number\"\x00\x12%\n\x06TellMe\x12\x08.WhatAmI\x1a\x0f.StringResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'foxy_grpc.pb2.strings_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_STRINGREQUEST']._serialized_start=31
  _globals['_STRINGREQUEST']._serialized_end=96
  _globals['_STRINGRESPONSE']._serialized_start=98
  _globals['_STRINGRESPONSE']._serialized_end=131
  _globals['_EMPTYMESSAGE']._serialized_start=133
  _globals['_EMPTYMESSAGE']._serialized_end=147
  _globals['_NUMBER']._serialized_start=149
  _globals['_NUMBER']._serialized_end=172
  _globals['_WHATAMI']._serialized_start=174
  _globals['_WHATAMI']._serialized_end=226
  _globals['_STRINGSERVICE']._serialized_start=229
  _globals['_STRINGSERVICE']._serialized_end=405
# @@protoc_insertion_point(module_scope)
