# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ndk/interface_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from ndk import sdk_common_pb2 as ndk_dot_sdk__common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ndk/interface_service.proto',
  package='srlinux.sdk',
  syntax='proto3',
  serialized_options=b'Z#github.com/nokia/srlinux-ndk-go/ndk',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1bndk/interface_service.proto\x12\x0bsrlinux.sdk\x1a\x14ndk/sdk_common.proto\"F\n\x1cInterfaceSubscriptionRequest\x12&\n\x03key\x18\x01 \x01(\x0b\x32\x19.srlinux.sdk.InterfaceKey\"\x1f\n\x0cInterfaceKey\x12\x0f\n\x07if_name\x18\x01 \x01(\t\"\xf0\x01\n\rInterfaceData\x12\x13\n\x0b\x61\x64min_is_up\x18\x01 \x01(\r\x12\x0b\n\x03mtu\x18\x02 \x01(\r\x12)\n\x07if_type\x18\x03 \x01(\x0e\x32\x18.srlinux.sdk.IfMgrIfType\x12&\n\x07port_id\x18\x04 \x01(\x0b\x32\x15.srlinux.sdk.PortIdPb\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12+\n\x08mac_addr\x18\x06 \x01(\x0b\x32\x19.srlinux.sdk.MacAddressPb\x12\x14\n\x0c\x61ggregate_id\x18\x07 \x01(\t\x12\x12\n\noper_is_up\x18\x08 \x01(\r\"\x93\x01\n\x15InterfaceNotification\x12(\n\x02op\x18\x01 \x01(\x0e\x32\x1c.srlinux.sdk.SdkMgrOperation\x12&\n\x03key\x18\x02 \x01(\x0b\x32\x19.srlinux.sdk.InterfaceKey\x12(\n\x04\x64\x61ta\x18\x03 \x01(\x0b\x32\x1a.srlinux.sdk.InterfaceDataB%Z#github.com/nokia/srlinux-ndk-go/ndkb\x06proto3'
  ,
  dependencies=[ndk_dot_sdk__common__pb2.DESCRIPTOR,])




_INTERFACESUBSCRIPTIONREQUEST = _descriptor.Descriptor(
  name='InterfaceSubscriptionRequest',
  full_name='srlinux.sdk.InterfaceSubscriptionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='srlinux.sdk.InterfaceSubscriptionRequest.key', index=0,
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
  serialized_start=66,
  serialized_end=136,
)


_INTERFACEKEY = _descriptor.Descriptor(
  name='InterfaceKey',
  full_name='srlinux.sdk.InterfaceKey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='if_name', full_name='srlinux.sdk.InterfaceKey.if_name', index=0,
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
  serialized_start=138,
  serialized_end=169,
)


_INTERFACEDATA = _descriptor.Descriptor(
  name='InterfaceData',
  full_name='srlinux.sdk.InterfaceData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='admin_is_up', full_name='srlinux.sdk.InterfaceData.admin_is_up', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mtu', full_name='srlinux.sdk.InterfaceData.mtu', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='if_type', full_name='srlinux.sdk.InterfaceData.if_type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='port_id', full_name='srlinux.sdk.InterfaceData.port_id', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='srlinux.sdk.InterfaceData.description', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mac_addr', full_name='srlinux.sdk.InterfaceData.mac_addr', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='aggregate_id', full_name='srlinux.sdk.InterfaceData.aggregate_id', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='oper_is_up', full_name='srlinux.sdk.InterfaceData.oper_is_up', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=172,
  serialized_end=412,
)


_INTERFACENOTIFICATION = _descriptor.Descriptor(
  name='InterfaceNotification',
  full_name='srlinux.sdk.InterfaceNotification',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='op', full_name='srlinux.sdk.InterfaceNotification.op', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='key', full_name='srlinux.sdk.InterfaceNotification.key', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='srlinux.sdk.InterfaceNotification.data', index=2,
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
  serialized_start=415,
  serialized_end=562,
)

_INTERFACESUBSCRIPTIONREQUEST.fields_by_name['key'].message_type = _INTERFACEKEY
_INTERFACEDATA.fields_by_name['if_type'].enum_type = ndk_dot_sdk__common__pb2._IFMGRIFTYPE
_INTERFACEDATA.fields_by_name['port_id'].message_type = ndk_dot_sdk__common__pb2._PORTIDPB
_INTERFACEDATA.fields_by_name['mac_addr'].message_type = ndk_dot_sdk__common__pb2._MACADDRESSPB
_INTERFACENOTIFICATION.fields_by_name['op'].enum_type = ndk_dot_sdk__common__pb2._SDKMGROPERATION
_INTERFACENOTIFICATION.fields_by_name['key'].message_type = _INTERFACEKEY
_INTERFACENOTIFICATION.fields_by_name['data'].message_type = _INTERFACEDATA
DESCRIPTOR.message_types_by_name['InterfaceSubscriptionRequest'] = _INTERFACESUBSCRIPTIONREQUEST
DESCRIPTOR.message_types_by_name['InterfaceKey'] = _INTERFACEKEY
DESCRIPTOR.message_types_by_name['InterfaceData'] = _INTERFACEDATA
DESCRIPTOR.message_types_by_name['InterfaceNotification'] = _INTERFACENOTIFICATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InterfaceSubscriptionRequest = _reflection.GeneratedProtocolMessageType('InterfaceSubscriptionRequest', (_message.Message,), {
  'DESCRIPTOR' : _INTERFACESUBSCRIPTIONREQUEST,
  '__module__' : 'ndk.interface_service_pb2'
  # @@protoc_insertion_point(class_scope:srlinux.sdk.InterfaceSubscriptionRequest)
  })
_sym_db.RegisterMessage(InterfaceSubscriptionRequest)

InterfaceKey = _reflection.GeneratedProtocolMessageType('InterfaceKey', (_message.Message,), {
  'DESCRIPTOR' : _INTERFACEKEY,
  '__module__' : 'ndk.interface_service_pb2'
  # @@protoc_insertion_point(class_scope:srlinux.sdk.InterfaceKey)
  })
_sym_db.RegisterMessage(InterfaceKey)

InterfaceData = _reflection.GeneratedProtocolMessageType('InterfaceData', (_message.Message,), {
  'DESCRIPTOR' : _INTERFACEDATA,
  '__module__' : 'ndk.interface_service_pb2'
  # @@protoc_insertion_point(class_scope:srlinux.sdk.InterfaceData)
  })
_sym_db.RegisterMessage(InterfaceData)

InterfaceNotification = _reflection.GeneratedProtocolMessageType('InterfaceNotification', (_message.Message,), {
  'DESCRIPTOR' : _INTERFACENOTIFICATION,
  '__module__' : 'ndk.interface_service_pb2'
  # @@protoc_insertion_point(class_scope:srlinux.sdk.InterfaceNotification)
  })
_sym_db.RegisterMessage(InterfaceNotification)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
