# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: airflow.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='airflow.proto',
  package='service',
  syntax='proto3',
  serialized_pb=_b('\n\rairflow.proto\x12\x07service\"!\n\x0bReqPingData\x12\x12\n\nhealth_url\x18\x01 \x01(\t\"\x1e\n\x0cRespPingData\x12\x0e\n\x06status\x18\x01 \x01(\t\"R\n\rReqDeployData\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x14\n\x0cservice_name\x18\x03 \x01(\t\x12\x0c\n\x04port\x18\x04 \x01(\x05\"k\n\x0eRespDeployData\x12-\n\x03ret\x18\x01 \x03(\x0b\x32 .service.RespDeployData.RetEntry\x1a*\n\x08RetEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"%\n\x0fReqCheckSvcData\x12\x12\n\nhealth_url\x18\x01 \x01(\t\"\"\n\x10RespCheckSvcData\x12\x0e\n\x06status\x18\x01 \x01(\t2=\n\x04Ping\x12\x35\n\x04Ping\x12\x14.service.ReqPingData\x1a\x15.service.RespPingData\"\x00\x32\x45\n\x06\x44\x65ploy\x12;\n\x06\x44\x65ploy\x12\x16.service.ReqDeployData\x1a\x17.service.RespDeployData\"\x00\x32U\n\x0cServiceCheck\x12\x45\n\x0cServiceCheck\x12\x18.service.ReqCheckSvcData\x1a\x19.service.RespCheckSvcData\"\x00\x62\x06proto3')
)




_REQPINGDATA = _descriptor.Descriptor(
  name='ReqPingData',
  full_name='service.ReqPingData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='health_url', full_name='service.ReqPingData.health_url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=26,
  serialized_end=59,
)


_RESPPINGDATA = _descriptor.Descriptor(
  name='RespPingData',
  full_name='service.RespPingData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='service.RespPingData.status', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=61,
  serialized_end=91,
)


_REQDEPLOYDATA = _descriptor.Descriptor(
  name='ReqDeployData',
  full_name='service.ReqDeployData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='service.ReqDeployData.version', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='service.ReqDeployData.type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='service_name', full_name='service.ReqDeployData.service_name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='port', full_name='service.ReqDeployData.port', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=93,
  serialized_end=175,
)


_RESPDEPLOYDATA_RETENTRY = _descriptor.Descriptor(
  name='RetEntry',
  full_name='service.RespDeployData.RetEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='service.RespDeployData.RetEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='service.RespDeployData.RetEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=242,
  serialized_end=284,
)

_RESPDEPLOYDATA = _descriptor.Descriptor(
  name='RespDeployData',
  full_name='service.RespDeployData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ret', full_name='service.RespDeployData.ret', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_RESPDEPLOYDATA_RETENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=177,
  serialized_end=284,
)


_REQCHECKSVCDATA = _descriptor.Descriptor(
  name='ReqCheckSvcData',
  full_name='service.ReqCheckSvcData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='health_url', full_name='service.ReqCheckSvcData.health_url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=286,
  serialized_end=323,
)


_RESPCHECKSVCDATA = _descriptor.Descriptor(
  name='RespCheckSvcData',
  full_name='service.RespCheckSvcData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='service.RespCheckSvcData.status', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=325,
  serialized_end=359,
)

_RESPDEPLOYDATA_RETENTRY.containing_type = _RESPDEPLOYDATA
_RESPDEPLOYDATA.fields_by_name['ret'].message_type = _RESPDEPLOYDATA_RETENTRY
DESCRIPTOR.message_types_by_name['ReqPingData'] = _REQPINGDATA
DESCRIPTOR.message_types_by_name['RespPingData'] = _RESPPINGDATA
DESCRIPTOR.message_types_by_name['ReqDeployData'] = _REQDEPLOYDATA
DESCRIPTOR.message_types_by_name['RespDeployData'] = _RESPDEPLOYDATA
DESCRIPTOR.message_types_by_name['ReqCheckSvcData'] = _REQCHECKSVCDATA
DESCRIPTOR.message_types_by_name['RespCheckSvcData'] = _RESPCHECKSVCDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ReqPingData = _reflection.GeneratedProtocolMessageType('ReqPingData', (_message.Message,), dict(
  DESCRIPTOR = _REQPINGDATA,
  __module__ = 'airflow_pb2'
  # @@protoc_insertion_point(class_scope:service.ReqPingData)
  ))
_sym_db.RegisterMessage(ReqPingData)

RespPingData = _reflection.GeneratedProtocolMessageType('RespPingData', (_message.Message,), dict(
  DESCRIPTOR = _RESPPINGDATA,
  __module__ = 'airflow_pb2'
  # @@protoc_insertion_point(class_scope:service.RespPingData)
  ))
_sym_db.RegisterMessage(RespPingData)

ReqDeployData = _reflection.GeneratedProtocolMessageType('ReqDeployData', (_message.Message,), dict(
  DESCRIPTOR = _REQDEPLOYDATA,
  __module__ = 'airflow_pb2'
  # @@protoc_insertion_point(class_scope:service.ReqDeployData)
  ))
_sym_db.RegisterMessage(ReqDeployData)

RespDeployData = _reflection.GeneratedProtocolMessageType('RespDeployData', (_message.Message,), dict(

  RetEntry = _reflection.GeneratedProtocolMessageType('RetEntry', (_message.Message,), dict(
    DESCRIPTOR = _RESPDEPLOYDATA_RETENTRY,
    __module__ = 'airflow_pb2'
    # @@protoc_insertion_point(class_scope:service.RespDeployData.RetEntry)
    ))
  ,
  DESCRIPTOR = _RESPDEPLOYDATA,
  __module__ = 'airflow_pb2'
  # @@protoc_insertion_point(class_scope:service.RespDeployData)
  ))
_sym_db.RegisterMessage(RespDeployData)
_sym_db.RegisterMessage(RespDeployData.RetEntry)

ReqCheckSvcData = _reflection.GeneratedProtocolMessageType('ReqCheckSvcData', (_message.Message,), dict(
  DESCRIPTOR = _REQCHECKSVCDATA,
  __module__ = 'airflow_pb2'
  # @@protoc_insertion_point(class_scope:service.ReqCheckSvcData)
  ))
_sym_db.RegisterMessage(ReqCheckSvcData)

RespCheckSvcData = _reflection.GeneratedProtocolMessageType('RespCheckSvcData', (_message.Message,), dict(
  DESCRIPTOR = _RESPCHECKSVCDATA,
  __module__ = 'airflow_pb2'
  # @@protoc_insertion_point(class_scope:service.RespCheckSvcData)
  ))
_sym_db.RegisterMessage(RespCheckSvcData)


_RESPDEPLOYDATA_RETENTRY.has_options = True
_RESPDEPLOYDATA_RETENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))

_PING = _descriptor.ServiceDescriptor(
  name='Ping',
  full_name='service.Ping',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=361,
  serialized_end=422,
  methods=[
  _descriptor.MethodDescriptor(
    name='Ping',
    full_name='service.Ping.Ping',
    index=0,
    containing_service=None,
    input_type=_REQPINGDATA,
    output_type=_RESPPINGDATA,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PING)

DESCRIPTOR.services_by_name['Ping'] = _PING


_DEPLOY = _descriptor.ServiceDescriptor(
  name='Deploy',
  full_name='service.Deploy',
  file=DESCRIPTOR,
  index=1,
  options=None,
  serialized_start=424,
  serialized_end=493,
  methods=[
  _descriptor.MethodDescriptor(
    name='Deploy',
    full_name='service.Deploy.Deploy',
    index=0,
    containing_service=None,
    input_type=_REQDEPLOYDATA,
    output_type=_RESPDEPLOYDATA,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_DEPLOY)

DESCRIPTOR.services_by_name['Deploy'] = _DEPLOY


_SERVICECHECK = _descriptor.ServiceDescriptor(
  name='ServiceCheck',
  full_name='service.ServiceCheck',
  file=DESCRIPTOR,
  index=2,
  options=None,
  serialized_start=495,
  serialized_end=580,
  methods=[
  _descriptor.MethodDescriptor(
    name='ServiceCheck',
    full_name='service.ServiceCheck.ServiceCheck',
    index=0,
    containing_service=None,
    input_type=_REQCHECKSVCDATA,
    output_type=_RESPCHECKSVCDATA,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SERVICECHECK)

DESCRIPTOR.services_by_name['ServiceCheck'] = _SERVICECHECK

# @@protoc_insertion_point(module_scope)
