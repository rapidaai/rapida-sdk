from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import any_pb2 as _any_pb2
import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar, Iterable, Mapping, Optional, Text, Union

DESCRIPTOR: _descriptor.FileDescriptor

class CallerResponse(_message.Message):
    __slots__ = ["error", "metrics", "requestId", "response", "responses", "timeTaken"]
    ERROR_FIELD_NUMBER: ClassVar[int]
    METRICS_FIELD_NUMBER: ClassVar[int]
    REQUESTID_FIELD_NUMBER: ClassVar[int]
    RESPONSES_FIELD_NUMBER: ClassVar[int]
    RESPONSE_FIELD_NUMBER: ClassVar[int]
    TIMETAKEN_FIELD_NUMBER: ClassVar[int]
    error: InvokerError
    metrics: _containers.RepeatedCompositeFieldContainer[_common_pb2.Metric]
    requestId: int
    response: str
    responses: _containers.RepeatedCompositeFieldContainer[_common_pb2.Content]
    timeTaken: int
    def __init__(self, requestId: Optional[int] = ..., response: Optional[str] = ..., timeTaken: Optional[int] = ..., responses: Optional[Iterable[Union[_common_pb2.Content, Mapping]]] = ..., error: Optional[Union[InvokerError, Mapping]] = ..., metrics: Optional[Iterable[Union[_common_pb2.Metric, Mapping]]] = ...) -> None: ...

class EndpointDefinition(_message.Message):
    __slots__ = ["endpointId", "version"]
    ENDPOINTID_FIELD_NUMBER: ClassVar[int]
    VERSION_FIELD_NUMBER: ClassVar[int]
    endpointId: int
    version: str
    def __init__(self, endpointId: Optional[int] = ..., version: Optional[str] = ...) -> None: ...

class InvokeRequest(_message.Message):
    __slots__ = ["args", "argsV1", "endpoint", "metadata", "options"]
    class ArgsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: ClassVar[int]
        VALUE_FIELD_NUMBER: ClassVar[int]
        key: str
        value: _any_pb2.Any
        def __init__(self, key: Optional[str] = ..., value: Optional[Union[_any_pb2.Any, Mapping]] = ...) -> None: ...
    class ArgsV1Entry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: ClassVar[int]
        VALUE_FIELD_NUMBER: ClassVar[int]
        key: str
        value: str
        def __init__(self, key: Optional[str] = ..., value: Optional[str] = ...) -> None: ...
    class MetadataEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: ClassVar[int]
        VALUE_FIELD_NUMBER: ClassVar[int]
        key: str
        value: str
        def __init__(self, key: Optional[str] = ..., value: Optional[str] = ...) -> None: ...
    class OptionsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: ClassVar[int]
        VALUE_FIELD_NUMBER: ClassVar[int]
        key: str
        value: str
        def __init__(self, key: Optional[str] = ..., value: Optional[str] = ...) -> None: ...
    ARGSV1_FIELD_NUMBER: ClassVar[int]
    ARGS_FIELD_NUMBER: ClassVar[int]
    ENDPOINT_FIELD_NUMBER: ClassVar[int]
    METADATA_FIELD_NUMBER: ClassVar[int]
    OPTIONS_FIELD_NUMBER: ClassVar[int]
    args: _containers.MessageMap[str, _any_pb2.Any]
    argsV1: _containers.ScalarMap[str, str]
    endpoint: EndpointDefinition
    metadata: _containers.ScalarMap[str, str]
    options: _containers.ScalarMap[str, str]
    def __init__(self, endpoint: Optional[Union[EndpointDefinition, Mapping]] = ..., argsV1: Optional[Mapping[str, str]] = ..., metadata: Optional[Mapping[str, str]] = ..., options: Optional[Mapping[str, str]] = ..., args: Optional[Mapping[str, _any_pb2.Any]] = ...) -> None: ...

class InvokeResponse(_message.Message):
    __slots__ = ["code", "data", "error", "success"]
    CODE_FIELD_NUMBER: ClassVar[int]
    DATA_FIELD_NUMBER: ClassVar[int]
    ERROR_FIELD_NUMBER: ClassVar[int]
    SUCCESS_FIELD_NUMBER: ClassVar[int]
    code: int
    data: CallerResponse
    error: InvokerError
    success: bool
    def __init__(self, code: Optional[int] = ..., success: bool = ..., data: Optional[Union[CallerResponse, Mapping]] = ..., error: Optional[Union[InvokerError, Mapping]] = ...) -> None: ...

class InvokerError(_message.Message):
    __slots__ = ["errorCode", "errorMessage", "humanMessage"]
    ERRORCODE_FIELD_NUMBER: ClassVar[int]
    ERRORMESSAGE_FIELD_NUMBER: ClassVar[int]
    HUMANMESSAGE_FIELD_NUMBER: ClassVar[int]
    errorCode: int
    errorMessage: str
    humanMessage: str
    def __init__(self, errorCode: Optional[int] = ..., errorMessage: Optional[str] = ..., humanMessage: Optional[str] = ...) -> None: ...

class ProbeRequest(_message.Message):
    __slots__ = ["requestId"]
    REQUESTID_FIELD_NUMBER: ClassVar[int]
    requestId: int
    def __init__(self, requestId: Optional[int] = ...) -> None: ...

class ProbeResponse(_message.Message):
    __slots__ = ["code", "data", "error", "success"]
    CODE_FIELD_NUMBER: ClassVar[int]
    DATA_FIELD_NUMBER: ClassVar[int]
    ERROR_FIELD_NUMBER: ClassVar[int]
    SUCCESS_FIELD_NUMBER: ClassVar[int]
    code: int
    data: _struct_pb2.Struct
    error: InvokerError
    success: bool
    def __init__(self, code: Optional[int] = ..., success: bool = ..., data: Optional[Union[_struct_pb2.Struct, Mapping]] = ..., error: Optional[Union[InvokerError, Mapping]] = ...) -> None: ...

class UpdateRequest(_message.Message):
    __slots__ = ["metadata", "requestId"]
    METADATA_FIELD_NUMBER: ClassVar[int]
    REQUESTID_FIELD_NUMBER: ClassVar[int]
    metadata: _struct_pb2.Struct
    requestId: int
    def __init__(self, requestId: Optional[int] = ..., metadata: Optional[Union[_struct_pb2.Struct, Mapping]] = ...) -> None: ...

class UpdateResponse(_message.Message):
    __slots__ = ["code", "error", "success"]
    CODE_FIELD_NUMBER: ClassVar[int]
    ERROR_FIELD_NUMBER: ClassVar[int]
    SUCCESS_FIELD_NUMBER: ClassVar[int]
    code: int
    error: InvokerError
    success: bool
    def __init__(self, code: Optional[int] = ..., success: bool = ..., error: Optional[Union[InvokerError, Mapping]] = ...) -> None: ...
