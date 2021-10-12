# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ndk/telemetry_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ndk import sdk_common_pb2 as ndk_dot_sdk__common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ndk/telemetry_service.proto',
  package='ndk',
  syntax='proto3',
  serialized_options=b'Z#github.com/nokia/srlinux-ndk-go/ndk',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1bndk/telemetry_service.proto\x12\x03ndk\x1a\x14ndk/sdk_common.proto\"\x1f\n\x0cTelemetryKey\x12\x0f\n\x07js_path\x18\x01 \x01(\t\"%\n\rTelemetryData\x12\x14\n\x0cjson_content\x18\x01 \x01(\t\"Q\n\rTelemetryInfo\x12\x1e\n\x03key\x18\x01 \x01(\x0b\x32\x11.ndk.TelemetryKey\x12 \n\x04\x64\x61ta\x18\x02 \x01(\x0b\x32\x12.ndk.TelemetryData\";\n\x16TelemetryUpdateRequest\x12!\n\x05state\x18\x01 \x03(\x0b\x32\x12.ndk.TelemetryInfo\"O\n\x17TelemetryUpdateResponse\x12!\n\x06status\x18\x01 \x01(\x0e\x32\x11.ndk.SdkMgrStatus\x12\x11\n\terror_str\x18\x02 \x01(\t\"8\n\x16TelemetryDeleteRequest\x12\x1e\n\x03key\x18\x01 \x03(\x0b\x32\x11.ndk.TelemetryKey\"O\n\x17TelemetryDeleteResponse\x12!\n\x06status\x18\x01 \x01(\x0e\x32\x11.ndk.SdkMgrStatus\x12\x11\n\terror_str\x18\x02 \x01(\t2\xbd\x01\n\x16SdkMgrTelemetryService\x12S\n\x14TelemetryAddOrUpdate\x12\x1b.ndk.TelemetryUpdateRequest\x1a\x1c.ndk.TelemetryUpdateResponse\"\x00\x12N\n\x0fTelemetryDelete\x12\x1b.ndk.TelemetryDeleteRequest\x1a\x1c.ndk.TelemetryDeleteResponse\"\x00\x42%Z#github.com/nokia/srlinux-ndk-go/ndkb\x06proto3'
  ,
  dependencies=[ndk_dot_sdk__common__pb2.DESCRIPTOR,])




_TELEMETRYKEY = _descriptor.Descriptor(
  name='TelemetryKey',
  full_name='ndk.TelemetryKey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='js_path', full_name='ndk.TelemetryKey.js_path', index=0,
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
  serialized_start=58,
  serialized_end=89,
)


_TELEMETRYDATA = _descriptor.Descriptor(
  name='TelemetryData',
  full_name='ndk.TelemetryData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='json_content', full_name='ndk.TelemetryData.json_content', index=0,
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
  serialized_start=91,
  serialized_end=128,
)


_TELEMETRYINFO = _descriptor.Descriptor(
  name='TelemetryInfo',
  full_name='ndk.TelemetryInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='ndk.TelemetryInfo.key', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='ndk.TelemetryInfo.data', index=1,
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
  serialized_start=130,
  serialized_end=211,
)


_TELEMETRYUPDATEREQUEST = _descriptor.Descriptor(
  name='TelemetryUpdateRequest',
  full_name='ndk.TelemetryUpdateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='state', full_name='ndk.TelemetryUpdateRequest.state', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=213,
  serialized_end=272,
)


_TELEMETRYUPDATERESPONSE = _descriptor.Descriptor(
  name='TelemetryUpdateResponse',
  full_name='ndk.TelemetryUpdateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='ndk.TelemetryUpdateResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error_str', full_name='ndk.TelemetryUpdateResponse.error_str', index=1,
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
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=274,
  serialized_end=353,
)


_TELEMETRYDELETEREQUEST = _descriptor.Descriptor(
  name='TelemetryDeleteRequest',
  full_name='ndk.TelemetryDeleteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='ndk.TelemetryDeleteRequest.key', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=355,
  serialized_end=411,
)


_TELEMETRYDELETERESPONSE = _descriptor.Descriptor(
  name='TelemetryDeleteResponse',
  full_name='ndk.TelemetryDeleteResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='ndk.TelemetryDeleteResponse.status', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='error_str', full_name='ndk.TelemetryDeleteResponse.error_str', index=1,
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
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=413,
  serialized_end=492,
)

_TELEMETRYINFO.fields_by_name['key'].message_type = _TELEMETRYKEY
_TELEMETRYINFO.fields_by_name['data'].message_type = _TELEMETRYDATA
_TELEMETRYUPDATEREQUEST.fields_by_name['state'].message_type = _TELEMETRYINFO
_TELEMETRYUPDATERESPONSE.fields_by_name['status'].enum_type = ndk_dot_sdk__common__pb2._SDKMGRSTATUS
_TELEMETRYDELETEREQUEST.fields_by_name['key'].message_type = _TELEMETRYKEY
_TELEMETRYDELETERESPONSE.fields_by_name['status'].enum_type = ndk_dot_sdk__common__pb2._SDKMGRSTATUS
DESCRIPTOR.message_types_by_name['TelemetryKey'] = _TELEMETRYKEY
DESCRIPTOR.message_types_by_name['TelemetryData'] = _TELEMETRYDATA
DESCRIPTOR.message_types_by_name['TelemetryInfo'] = _TELEMETRYINFO
DESCRIPTOR.message_types_by_name['TelemetryUpdateRequest'] = _TELEMETRYUPDATEREQUEST
DESCRIPTOR.message_types_by_name['TelemetryUpdateResponse'] = _TELEMETRYUPDATERESPONSE
DESCRIPTOR.message_types_by_name['TelemetryDeleteRequest'] = _TELEMETRYDELETEREQUEST
DESCRIPTOR.message_types_by_name['TelemetryDeleteResponse'] = _TELEMETRYDELETERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TelemetryKey = _reflection.GeneratedProtocolMessageType('TelemetryKey', (_message.Message,), {
  'DESCRIPTOR' : _TELEMETRYKEY,
  '__module__' : 'ndk.telemetry_service_pb2'
  # @@protoc_insertion_point(class_scope:ndk.TelemetryKey)
  })
_sym_db.RegisterMessage(TelemetryKey)

TelemetryData = _reflection.GeneratedProtocolMessageType('TelemetryData', (_message.Message,), {
  'DESCRIPTOR' : _TELEMETRYDATA,
  '__module__' : 'ndk.telemetry_service_pb2'
  # @@protoc_insertion_point(class_scope:ndk.TelemetryData)
  })
_sym_db.RegisterMessage(TelemetryData)

TelemetryInfo = _reflection.GeneratedProtocolMessageType('TelemetryInfo', (_message.Message,), {
  'DESCRIPTOR' : _TELEMETRYINFO,
  '__module__' : 'ndk.telemetry_service_pb2'
  # @@protoc_insertion_point(class_scope:ndk.TelemetryInfo)
  })
_sym_db.RegisterMessage(TelemetryInfo)

TelemetryUpdateRequest = _reflection.GeneratedProtocolMessageType('TelemetryUpdateRequest', (_message.Message,), {
  'DESCRIPTOR' : _TELEMETRYUPDATEREQUEST,
  '__module__' : 'ndk.telemetry_service_pb2'
  # @@protoc_insertion_point(class_scope:ndk.TelemetryUpdateRequest)
  })
_sym_db.RegisterMessage(TelemetryUpdateRequest)

TelemetryUpdateResponse = _reflection.GeneratedProtocolMessageType('TelemetryUpdateResponse', (_message.Message,), {
  'DESCRIPTOR' : _TELEMETRYUPDATERESPONSE,
  '__module__' : 'ndk.telemetry_service_pb2'
  # @@protoc_insertion_point(class_scope:ndk.TelemetryUpdateResponse)
  })
_sym_db.RegisterMessage(TelemetryUpdateResponse)

TelemetryDeleteRequest = _reflection.GeneratedProtocolMessageType('TelemetryDeleteRequest', (_message.Message,), {
  'DESCRIPTOR' : _TELEMETRYDELETEREQUEST,
  '__module__' : 'ndk.telemetry_service_pb2'
  # @@protoc_insertion_point(class_scope:ndk.TelemetryDeleteRequest)
  })
_sym_db.RegisterMessage(TelemetryDeleteRequest)

TelemetryDeleteResponse = _reflection.GeneratedProtocolMessageType('TelemetryDeleteResponse', (_message.Message,), {
  'DESCRIPTOR' : _TELEMETRYDELETERESPONSE,
  '__module__' : 'ndk.telemetry_service_pb2'
  # @@protoc_insertion_point(class_scope:ndk.TelemetryDeleteResponse)
  })
_sym_db.RegisterMessage(TelemetryDeleteResponse)


DESCRIPTOR._options = None

_SDKMGRTELEMETRYSERVICE = _descriptor.ServiceDescriptor(
  name='SdkMgrTelemetryService',
  full_name='ndk.SdkMgrTelemetryService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=495,
  serialized_end=684,
  methods=[
  _descriptor.MethodDescriptor(
    name='TelemetryAddOrUpdate',
    full_name='ndk.SdkMgrTelemetryService.TelemetryAddOrUpdate',
    index=0,
    containing_service=None,
    input_type=_TELEMETRYUPDATEREQUEST,
    output_type=_TELEMETRYUPDATERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='TelemetryDelete',
    full_name='ndk.SdkMgrTelemetryService.TelemetryDelete',
    index=1,
    containing_service=None,
    input_type=_TELEMETRYDELETEREQUEST,
    output_type=_TELEMETRYDELETERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SDKMGRTELEMETRYSERVICE)

DESCRIPTOR.services_by_name['SdkMgrTelemetryService'] = _SDKMGRTELEMETRYSERVICE

# @@protoc_insertion_point(module_scope)
