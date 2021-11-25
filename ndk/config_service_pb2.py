# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ndk/config_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ndk import sdk_common_pb2 as ndk_dot_sdk__common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ndk/config_service.proto',
  package='srlinux.sdk',
  syntax='proto3',
  serialized_options=b'Z#github.com/nokia/srlinux-ndk-go/ndk',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x18ndk/config_service.proto\x12\x0bsrlinux.sdk\x1a\x14ndk/sdk_common.proto\"@\n\x19\x43onfigSubscriptionRequest\x12#\n\x03key\x18\x01 \x01(\x0b\x32\x16.srlinux.sdk.ConfigKey\"*\n\tConfigKey\x12\x0f\n\x07js_path\x18\x01 \x01(\t\x12\x0c\n\x04keys\x18\x02 \x03(\t\"\x1a\n\nConfigData\x12\x0c\n\x04json\x18\x01 \x01(\t\"\x8a\x01\n\x12\x43onfigNotification\x12(\n\x02op\x18\x01 \x01(\x0e\x32\x1c.srlinux.sdk.SdkMgrOperation\x12#\n\x03key\x18\x02 \x01(\x0b\x32\x16.srlinux.sdk.ConfigKey\x12%\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32\x17.srlinux.sdk.ConfigDataB%Z#github.com/nokia/srlinux-ndk-go/ndkb\x06proto3'
  ,
  dependencies=[ndk_dot_sdk__common__pb2.DESCRIPTOR,])




_CONFIGSUBSCRIPTIONREQUEST = _descriptor.Descriptor(
  name='ConfigSubscriptionRequest',
  full_name='srlinux.sdk.ConfigSubscriptionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='srlinux.sdk.ConfigSubscriptionRequest.key', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=63,
  serialized_end=127,
)


_CONFIGKEY = _descriptor.Descriptor(
  name='ConfigKey',
  full_name='srlinux.sdk.ConfigKey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='js_path', full_name='srlinux.sdk.ConfigKey.js_path', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='keys', full_name='srlinux.sdk.ConfigKey.keys', index=1,
      number=2, type=9, cpp_type=9, label=3,
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
  serialized_start=129,
  serialized_end=171,
)


_CONFIGDATA = _descriptor.Descriptor(
  name='ConfigData',
  full_name='srlinux.sdk.ConfigData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='json', full_name='srlinux.sdk.ConfigData.json', index=0,
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
  serialized_start=173,
  serialized_end=199,
)


_CONFIGNOTIFICATION = _descriptor.Descriptor(
  name='ConfigNotification',
  full_name='srlinux.sdk.ConfigNotification',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='op', full_name='srlinux.sdk.ConfigNotification.op', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='key', full_name='srlinux.sdk.ConfigNotification.key', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='srlinux.sdk.ConfigNotification.data', index=2,
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
  ],
  serialized_start=202,
  serialized_end=340,
)

_CONFIGSUBSCRIPTIONREQUEST.fields_by_name['key'].message_type = _CONFIGKEY
_CONFIGNOTIFICATION.fields_by_name['op'].enum_type = ndk_dot_sdk__common__pb2._SDKMGROPERATION
_CONFIGNOTIFICATION.fields_by_name['key'].message_type = _CONFIGKEY
_CONFIGNOTIFICATION.fields_by_name['data'].message_type = _CONFIGDATA
DESCRIPTOR.message_types_by_name['ConfigSubscriptionRequest'] = _CONFIGSUBSCRIPTIONREQUEST
DESCRIPTOR.message_types_by_name['ConfigKey'] = _CONFIGKEY
DESCRIPTOR.message_types_by_name['ConfigData'] = _CONFIGDATA
DESCRIPTOR.message_types_by_name['ConfigNotification'] = _CONFIGNOTIFICATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ConfigSubscriptionRequest = _reflection.GeneratedProtocolMessageType('ConfigSubscriptionRequest', (_message.Message,), {
  'DESCRIPTOR' : _CONFIGSUBSCRIPTIONREQUEST,
  '__module__' : 'ndk.config_service_pb2'
  # @@protoc_insertion_point(class_scope:srlinux.sdk.ConfigSubscriptionRequest)
  })
_sym_db.RegisterMessage(ConfigSubscriptionRequest)

ConfigKey = _reflection.GeneratedProtocolMessageType('ConfigKey', (_message.Message,), {
  'DESCRIPTOR' : _CONFIGKEY,
  '__module__' : 'ndk.config_service_pb2'
  # @@protoc_insertion_point(class_scope:srlinux.sdk.ConfigKey)
  })
_sym_db.RegisterMessage(ConfigKey)

ConfigData = _reflection.GeneratedProtocolMessageType('ConfigData', (_message.Message,), {
  'DESCRIPTOR' : _CONFIGDATA,
  '__module__' : 'ndk.config_service_pb2'
  # @@protoc_insertion_point(class_scope:srlinux.sdk.ConfigData)
  })
_sym_db.RegisterMessage(ConfigData)

ConfigNotification = _reflection.GeneratedProtocolMessageType('ConfigNotification', (_message.Message,), {
  'DESCRIPTOR' : _CONFIGNOTIFICATION,
  '__module__' : 'ndk.config_service_pb2'
  # @@protoc_insertion_point(class_scope:srlinux.sdk.ConfigNotification)
  })
_sym_db.RegisterMessage(ConfigNotification)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
