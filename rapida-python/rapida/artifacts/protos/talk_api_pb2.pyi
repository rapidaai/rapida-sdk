from google.protobuf import timestamp_pb2 as _timestamp_pb2
import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RAGStage(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UNDEFINED_STAGE: _ClassVar[RAGStage]
    QUERY_FORMULATION: _ClassVar[RAGStage]
    INFORMATION_RETRIEVAL: _ClassVar[RAGStage]
    DOCUMENT_RETRIEVAL: _ClassVar[RAGStage]
    CONTEXT_AUGMENTATION: _ClassVar[RAGStage]
    TEXT_GENERATION: _ClassVar[RAGStage]
    OUTPUT_EVALUATION: _ClassVar[RAGStage]
UNDEFINED_STAGE: RAGStage
QUERY_FORMULATION: RAGStage
INFORMATION_RETRIEVAL: RAGStage
DOCUMENT_RETRIEVAL: RAGStage
CONTEXT_AUGMENTATION: RAGStage
TEXT_GENERATION: RAGStage
OUTPUT_EVALUATION: RAGStage

class AssistantConversactionMessage(_message.Message):
    __slots__ = ("id", "assistantConversactionId", "requestRole", "request", "responseRole", "response", "externalAuditId", "source", "metrics", "status", "createdBy", "updatedBy", "suggestedQuestions", "stages", "createdDate", "updatedDate")
    ID_FIELD_NUMBER: _ClassVar[int]
    ASSISTANTCONVERSACTIONID_FIELD_NUMBER: _ClassVar[int]
    REQUESTROLE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    RESPONSEROLE_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    EXTERNALAUDITID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CREATEDBY_FIELD_NUMBER: _ClassVar[int]
    UPDATEDBY_FIELD_NUMBER: _ClassVar[int]
    SUGGESTEDQUESTIONS_FIELD_NUMBER: _ClassVar[int]
    STAGES_FIELD_NUMBER: _ClassVar[int]
    CREATEDDATE_FIELD_NUMBER: _ClassVar[int]
    UPDATEDDATE_FIELD_NUMBER: _ClassVar[int]
    id: int
    assistantConversactionId: int
    requestRole: str
    request: _common_pb2.Message
    responseRole: str
    response: _common_pb2.Message
    externalAuditId: int
    source: str
    metrics: _containers.RepeatedCompositeFieldContainer[_common_pb2.Metric]
    status: str
    createdBy: int
    updatedBy: int
    suggestedQuestions: _containers.RepeatedScalarFieldContainer[str]
    stages: _containers.RepeatedCompositeFieldContainer[AssistantMessageStage]
    createdDate: _timestamp_pb2.Timestamp
    updatedDate: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[int] = ..., assistantConversactionId: _Optional[int] = ..., requestRole: _Optional[str] = ..., request: _Optional[_Union[_common_pb2.Message, _Mapping]] = ..., responseRole: _Optional[str] = ..., response: _Optional[_Union[_common_pb2.Message, _Mapping]] = ..., externalAuditId: _Optional[int] = ..., source: _Optional[str] = ..., metrics: _Optional[_Iterable[_Union[_common_pb2.Metric, _Mapping]]] = ..., status: _Optional[str] = ..., createdBy: _Optional[int] = ..., updatedBy: _Optional[int] = ..., suggestedQuestions: _Optional[_Iterable[str]] = ..., stages: _Optional[_Iterable[_Union[AssistantMessageStage, _Mapping]]] = ..., createdDate: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updatedDate: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class CreateAssistantMessageRequest(_message.Message):
    __slots__ = ("assistantId", "assistantProviderModelId", "message", "assistantConversactionId")
    ASSISTANTID_FIELD_NUMBER: _ClassVar[int]
    ASSISTANTPROVIDERMODELID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ASSISTANTCONVERSACTIONID_FIELD_NUMBER: _ClassVar[int]
    assistantId: int
    assistantProviderModelId: int
    message: _common_pb2.Message
    assistantConversactionId: int
    def __init__(self, assistantId: _Optional[int] = ..., assistantProviderModelId: _Optional[int] = ..., message: _Optional[_Union[_common_pb2.Message, _Mapping]] = ..., assistantConversactionId: _Optional[int] = ...) -> None: ...

class AssistantMessageStage(_message.Message):
    __slots__ = ("stage", "additionalData", "timetaken")
    class AdditionalDataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    STAGE_FIELD_NUMBER: _ClassVar[int]
    ADDITIONALDATA_FIELD_NUMBER: _ClassVar[int]
    TIMETAKEN_FIELD_NUMBER: _ClassVar[int]
    stage: RAGStage
    additionalData: _containers.ScalarMap[str, str]
    timetaken: int
    def __init__(self, stage: _Optional[_Union[RAGStage, str]] = ..., additionalData: _Optional[_Mapping[str, str]] = ..., timetaken: _Optional[int] = ...) -> None: ...

class CreateAssistantMessageResponse(_message.Message):
    __slots__ = ("code", "success", "data", "error")
    CODE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    code: int
    success: bool
    data: AssistantConversactionMessage
    error: _common_pb2.Error
    def __init__(self, code: _Optional[int] = ..., success: bool = ..., data: _Optional[_Union[AssistantConversactionMessage, _Mapping]] = ..., error: _Optional[_Union[_common_pb2.Error, _Mapping]] = ...) -> None: ...

class AssistantConversaction(_message.Message):
    __slots__ = ("id", "userId", "assistantId", "name", "projectId", "organizationId", "source", "createdBy", "updatedBy", "user", "assistantProviderModelId", "assistantConversactionMessage", "createdDate", "updatedDate")
    ID_FIELD_NUMBER: _ClassVar[int]
    USERID_FIELD_NUMBER: _ClassVar[int]
    ASSISTANTID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PROJECTID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATIONID_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    CREATEDBY_FIELD_NUMBER: _ClassVar[int]
    UPDATEDBY_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    ASSISTANTPROVIDERMODELID_FIELD_NUMBER: _ClassVar[int]
    ASSISTANTCONVERSACTIONMESSAGE_FIELD_NUMBER: _ClassVar[int]
    CREATEDDATE_FIELD_NUMBER: _ClassVar[int]
    UPDATEDDATE_FIELD_NUMBER: _ClassVar[int]
    id: int
    userId: int
    assistantId: int
    name: str
    projectId: int
    organizationId: int
    source: str
    createdBy: int
    updatedBy: int
    user: _common_pb2.User
    assistantProviderModelId: int
    assistantConversactionMessage: _containers.RepeatedCompositeFieldContainer[AssistantConversactionMessage]
    createdDate: _timestamp_pb2.Timestamp
    updatedDate: _timestamp_pb2.Timestamp
    def __init__(self, id: _Optional[int] = ..., userId: _Optional[int] = ..., assistantId: _Optional[int] = ..., name: _Optional[str] = ..., projectId: _Optional[int] = ..., organizationId: _Optional[int] = ..., source: _Optional[str] = ..., createdBy: _Optional[int] = ..., updatedBy: _Optional[int] = ..., user: _Optional[_Union[_common_pb2.User, _Mapping]] = ..., assistantProviderModelId: _Optional[int] = ..., assistantConversactionMessage: _Optional[_Iterable[_Union[AssistantConversactionMessage, _Mapping]]] = ..., createdDate: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updatedDate: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class GetAllAssistantConversactionRequest(_message.Message):
    __slots__ = ("assistantId", "paginate", "criterias")
    ASSISTANTID_FIELD_NUMBER: _ClassVar[int]
    PAGINATE_FIELD_NUMBER: _ClassVar[int]
    CRITERIAS_FIELD_NUMBER: _ClassVar[int]
    assistantId: int
    paginate: _common_pb2.Paginate
    criterias: _containers.RepeatedCompositeFieldContainer[_common_pb2.Criteria]
    def __init__(self, assistantId: _Optional[int] = ..., paginate: _Optional[_Union[_common_pb2.Paginate, _Mapping]] = ..., criterias: _Optional[_Iterable[_Union[_common_pb2.Criteria, _Mapping]]] = ...) -> None: ...

class GetAllAssistantConversactionResponse(_message.Message):
    __slots__ = ("code", "success", "data", "error", "paginated")
    CODE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    PAGINATED_FIELD_NUMBER: _ClassVar[int]
    code: int
    success: bool
    data: _containers.RepeatedCompositeFieldContainer[AssistantConversaction]
    error: _common_pb2.Error
    paginated: _common_pb2.Paginated
    def __init__(self, code: _Optional[int] = ..., success: bool = ..., data: _Optional[_Iterable[_Union[AssistantConversaction, _Mapping]]] = ..., error: _Optional[_Union[_common_pb2.Error, _Mapping]] = ..., paginated: _Optional[_Union[_common_pb2.Paginated, _Mapping]] = ...) -> None: ...

class GetAllConversactionMessageRequest(_message.Message):
    __slots__ = ("assistantId", "assistantConversactionId", "paginate", "criterias", "order")
    ASSISTANTID_FIELD_NUMBER: _ClassVar[int]
    ASSISTANTCONVERSACTIONID_FIELD_NUMBER: _ClassVar[int]
    PAGINATE_FIELD_NUMBER: _ClassVar[int]
    CRITERIAS_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    assistantId: int
    assistantConversactionId: int
    paginate: _common_pb2.Paginate
    criterias: _containers.RepeatedCompositeFieldContainer[_common_pb2.Criteria]
    order: _common_pb2.Ordering
    def __init__(self, assistantId: _Optional[int] = ..., assistantConversactionId: _Optional[int] = ..., paginate: _Optional[_Union[_common_pb2.Paginate, _Mapping]] = ..., criterias: _Optional[_Iterable[_Union[_common_pb2.Criteria, _Mapping]]] = ..., order: _Optional[_Union[_common_pb2.Ordering, _Mapping]] = ...) -> None: ...

class GetAllConversactionMessageResponse(_message.Message):
    __slots__ = ("code", "success", "data", "error", "paginated")
    CODE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    PAGINATED_FIELD_NUMBER: _ClassVar[int]
    code: int
    success: bool
    data: _containers.RepeatedCompositeFieldContainer[AssistantConversactionMessage]
    error: _common_pb2.Error
    paginated: _common_pb2.Paginated
    def __init__(self, code: _Optional[int] = ..., success: bool = ..., data: _Optional[_Iterable[_Union[AssistantConversactionMessage, _Mapping]]] = ..., error: _Optional[_Union[_common_pb2.Error, _Mapping]] = ..., paginated: _Optional[_Union[_common_pb2.Paginated, _Mapping]] = ...) -> None: ...
