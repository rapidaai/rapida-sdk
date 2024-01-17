from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import any_pb2 as _any_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InvokerError(_message.Message):
    __slots__ = ("errorCode", "errorMessage", "humanMessage")
    ERRORCODE_FIELD_NUMBER: _ClassVar[int]
    ERRORMESSAGE_FIELD_NUMBER: _ClassVar[int]
    HUMANMESSAGE_FIELD_NUMBER: _ClassVar[int]
    errorCode: int
    errorMessage: str
    humanMessage: str
    def __init__(self, errorCode: _Optional[int] = ..., errorMessage: _Optional[str] = ..., humanMessage: _Optional[str] = ...) -> None: ...

class EndpointDefinition(_message.Message):
    __slots__ = ("endpointId", "version")
    ENDPOINTID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    endpointId: int
    version: str
    def __init__(self, endpointId: _Optional[int] = ..., version: _Optional[str] = ...) -> None: ...

class OverrideOption(_message.Message):
    __slots__ = ("name", "value")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: _any_pb2.Any
    def __init__(self, name: _Optional[str] = ..., value: _Optional[_Union[_any_pb2.Any, _Mapping]] = ...) -> None: ...

class InvokeRequest(_message.Message):
    __slots__ = ("endpoint", "args", "metadata", "options")
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    ARGS_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    endpoint: EndpointDefinition
    args: _struct_pb2.Struct
    metadata: _struct_pb2.Struct
    options: _struct_pb2.Struct
    def __init__(self, endpoint: _Optional[_Union[EndpointDefinition, _Mapping]] = ..., args: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., options: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class InvokeResponse(_message.Message):
    __slots__ = ("code", "success", "data", "error")
    CODE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    code: int
    success: bool
    data: _struct_pb2.Struct
    error: InvokerError
    def __init__(self, code: _Optional[int] = ..., success: bool = ..., data: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., error: _Optional[_Union[InvokerError, _Mapping]] = ...) -> None: ...

class UpdateRequest(_message.Message):
    __slots__ = ("requestId", "metadata")
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    requestId: int
    metadata: _struct_pb2.Struct
    def __init__(self, requestId: _Optional[int] = ..., metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class UpdateResponse(_message.Message):
    __slots__ = ("code", "success", "error")
    CODE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    code: int
    success: bool
    error: InvokerError
    def __init__(self, code: _Optional[int] = ..., success: bool = ..., error: _Optional[_Union[InvokerError, _Mapping]] = ...) -> None: ...

class ProbeRequest(_message.Message):
    __slots__ = ("requestId",)
    REQUESTID_FIELD_NUMBER: _ClassVar[int]
    requestId: int
    def __init__(self, requestId: _Optional[int] = ...) -> None: ...

class ProbeResponse(_message.Message):
    __slots__ = ("code", "success", "data", "error")
    CODE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    code: int
    success: bool
    data: _struct_pb2.Struct
    error: InvokerError
    def __init__(self, code: _Optional[int] = ..., success: bool = ..., data: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ..., error: _Optional[_Union[InvokerError, _Mapping]] = ...) -> None: ...
