# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ndk/networkinstance_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ndk import sdk_common_pb2 as ndk_dot_sdk__common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ndk/networkinstance_service.proto',
  package='srlinux.sdk',
  syntax='proto3',
  serialized_options=b'Z#github.com/nokia/srlinux-ndk-go/ndk',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n!ndk/networkinstance_service.proto\x12\x0bsrlinux.sdk\x1a\x14ndk/sdk_common.proto\"$\n\"NetworkInstanceSubscriptionRequest\"\'\n\x12NetworkInstanceKey\x12\x11\n\tinst_name\x18\x01 \x01(\t\"\x81\x02\n\x13NetworkInstanceData\x12\x13\n\x0bnet_inst_id\x18\x01 \x01(\r\x12\x11\n\tbase_name\x18\x02 \x01(\t\x12\x33\n\rloopback_addr\x18\x03 \x01(\x0b\x32\x1c.srlinux.sdk.IpAddrPrefLenPb\x12\x12\n\noper_is_up\x18\x04 \x01(\x08\x12\x11\n\trouter_id\x18\x05 \x01(\t\x12?\n\tinst_type\x18\x06 \x01(\x0e\x32,.srlinux.sdk.NetworkInstanceData.NetInstType\"%\n\x0bNetInstType\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\t\n\x05L3VRF\x10\x01\"\xa5\x01\n\x1bNetworkInstanceNotification\x12(\n\x02op\x18\x01 \x01(\x0e\x32\x1c.srlinux.sdk.SdkMgrOperation\x12,\n\x03key\x18\x02 \x01(\x0b\x32\x1f.srlinux.sdk.NetworkInstanceKey\x12.\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32 .srlinux.sdk.NetworkInstanceDataB%Z#github.com/nokia/srlinux-ndk-go/ndkb\x06proto3'
  ,
  dependencies=[ndk_dot_sdk__common__pb2.DESCRIPTOR,])



_NETWORKINSTANCEDATA_NETINSTTYPE = _descriptor.EnumDescriptor(
  name='NetInstType',
  full_name='srlinux.sdk.NetworkInstanceData.NetInstType',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DEFAULT', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='L3VRF', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=372,
  serialized_end=409,
)
_sym_db.RegisterEnumDescriptor(_NETWORKINSTANCEDATA_NETINSTTYPE)


_NETWORKINSTANCESUBSCRIPTIONREQUEST = _descriptor.Descriptor(
  name='NetworkInstanceSubscriptionRequest',
  full_name='srlinux.sdk.NetworkInstanceSubscriptionRequest',
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
  serialized_start=72,
  serialized_end=108,
)


_NETWORKINSTANCEKEY = _descriptor.Descriptor(
  name='NetworkInstanceKey',
  full_name='srlinux.sdk.NetworkInstanceKey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='inst_name', full_name='srlinux.sdk.NetworkInstanceKey.inst_name', index=0,
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
  serialized_start=110,
  serialized_end=149,
)


_NETWORKINSTANCEDATA = _descriptor.Descriptor(
  name='NetworkInstanceData',
  full_name='srlinux.sdk.NetworkInstanceData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='net_inst_id', full_name='srlinux.sdk.NetworkInstanceData.net_inst_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='base_name', full_name='srlinux.sdk.NetworkInstanceData.base_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='loopback_addr', full_name='srlinux.sdk.NetworkInstanceData.loopback_addr', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='oper_is_up', full_name='srlinux.sdk.NetworkInstanceData.oper_is_up', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='router_id', full_name='srlinux.sdk.NetworkInstanceData.router_id', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='inst_type', full_name='srlinux.sdk.NetworkInstanceData.inst_type', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _NETWORKINSTANCEDATA_NETINSTTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=152,
  serialized_end=409,
)


_NETWORKINSTANCENOTIFICATION = _descriptor.Descriptor(
  name='NetworkInstanceNotification',
  full_name='srlinux.sdk.NetworkInstanceNotification',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='op', full_name='srlinux.sdk.NetworkInstanceNotification.op', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='key', full_name='srlinux.sdk.NetworkInstanceNotification.key', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='srlinux.sdk.NetworkInstanceNotification.data', index=2,
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
  serialized_start=412,
  serialized_end=577,
)

_NETWORKINSTANCEDATA.fields_by_name['loopback_addr'].message_type = ndk_dot_sdk__common__pb2._IPADDRPREFLENPB
_NETWORKINSTANCEDATA.fields_by_name['inst_type'].enum_type = _NETWORKINSTANCEDATA_NETINSTTYPE
_NETWORKINSTANCEDATA_NETINSTTYPE.containing_type = _NETWORKINSTANCEDATA
_NETWORKINSTANCENOTIFICATION.fields_by_name['op'].enum_type = ndk_dot_sdk__common__pb2._SDKMGROPERATION
_NETWORKINSTANCENOTIFICATION.fields_by_name['key'].message_type = _NETWORKINSTANCEKEY
_NETWORKINSTANCENOTIFICATION.fields_by_name['data'].message_type = _NETWORKINSTANCEDATA
DESCRIPTOR.message_types_by_name['NetworkInstanceSubscriptionRequest'] = _NETWORKINSTANCESUBSCRIPTIONREQUEST
DESCRIPTOR.message_types_by_name['NetworkInstanceKey'] = _NETWORKINSTANCEKEY
DESCRIPTOR.message_types_by_name['NetworkInstanceData'] = _NETWORKINSTANCEDATA
DESCRIPTOR.message_types_by_name['NetworkInstanceNotification'] = _NETWORKINSTANCENOTIFICATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NetworkInstanceSubscriptionRequest = _reflection.GeneratedProtocolMessageType('NetworkInstanceSubscriptionRequest', (_message.Message,), {
  'DESCRIPTOR' : _NETWORKINSTANCESUBSCRIPTIONREQUEST,
  '__module__' : 'ndk.networkinstance_service_pb2'
  # @@protoc_insertion_point(class_scope:srlinux.sdk.NetworkInstanceSubscriptionRequest)
  })
_sym_db.RegisterMessage(NetworkInstanceSubscriptionRequest)

NetworkInstanceKey = _reflection.GeneratedProtocolMessageType('NetworkInstanceKey', (_message.Message,), {
  'DESCRIPTOR' : _NETWORKINSTANCEKEY,
  '__module__' : 'ndk.networkinstance_service_pb2'
  # @@protoc_insertion_point(class_scope:srlinux.sdk.NetworkInstanceKey)
  })
_sym_db.RegisterMessage(NetworkInstanceKey)

NetworkInstanceData = _reflection.GeneratedProtocolMessageType('NetworkInstanceData', (_message.Message,), {
  'DESCRIPTOR' : _NETWORKINSTANCEDATA,
  '__module__' : 'ndk.networkinstance_service_pb2'
  # @@protoc_insertion_point(class_scope:srlinux.sdk.NetworkInstanceData)
  })
_sym_db.RegisterMessage(NetworkInstanceData)

NetworkInstanceNotification = _reflection.GeneratedProtocolMessageType('NetworkInstanceNotification', (_message.Message,), {
  'DESCRIPTOR' : _NETWORKINSTANCENOTIFICATION,
  '__module__' : 'ndk.networkinstance_service_pb2'
  # @@protoc_insertion_point(class_scope:srlinux.sdk.NetworkInstanceNotification)
  })
_sym_db.RegisterMessage(NetworkInstanceNotification)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
