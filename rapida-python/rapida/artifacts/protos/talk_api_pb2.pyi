from google.protobuf import timestamp_pb2 as _timestamp_pb2
import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar, Iterable, Mapping, Optional, Text, Union

CONTEXT_AUGMENTATION: RAGStage
DESCRIPTOR: _descriptor.FileDescriptor
DOCUMENT_RETRIEVAL: RAGStage
INFORMATION_RETRIEVAL: RAGStage
OUTPUT_EVALUATION: RAGStage
QUERY_FORMULATION: RAGStage
TEXT_GENERATION: RAGStage
UNDEFINED_STAGE: RAGStage

class AssistantConversaction(_message.Message):
    __slots__ = ["assistantConversactionMessage", "assistantId", "assistantProviderModelId", "createdBy", "createdDate", "id", "name", "organizationId", "projectId", "source", "updatedBy", "updatedDate", "user", "userId"]
    ASSISTANTCONVERSACTIONMESSAGE_FIELD_NUMBER: ClassVar[int]
    ASSISTANTID_FIELD_NUMBER: ClassVar[int]
    ASSISTANTPROVIDERMODELID_FIELD_NUMBER: ClassVar[int]
    CREATEDBY_FIELD_NUMBER: ClassVar[int]
    CREATEDDATE_FIELD_NUMBER: ClassVar[int]
    ID_FIELD_NUMBER: ClassVar[int]
    NAME_FIELD_NUMBER: ClassVar[int]
    ORGANIZATIONID_FIELD_NUMBER: ClassVar[int]
    PROJECTID_FIELD_NUMBER: ClassVar[int]
    SOURCE_FIELD_NUMBER: ClassVar[int]
    UPDATEDBY_FIELD_NUMBER: ClassVar[int]
    UPDATEDDATE_FIELD_NUMBER: ClassVar[int]
    USERID_FIELD_NUMBER: ClassVar[int]
    USER_FIELD_NUMBER: ClassVar[int]
    assistantConversactionMessage: _containers.RepeatedCompositeFieldContainer[AssistantConversactionMessage]
    assistantId: int
    assistantProviderModelId: int
    createdBy: int
    createdDate: _timestamp_pb2.Timestamp
    id: int
    name: str
    organizationId: int
    projectId: int
    source: str
    updatedBy: int
    updatedDate: _timestamp_pb2.Timestamp
    user: _common_pb2.User
    userId: int
    def __init__(self, id: Optional[int] = ..., userId: Optional[int] = ..., assistantId: Optional[int] = ..., name: Optional[str] = ..., projectId: Optional[int] = ..., organizationId: Optional[int] = ..., source: Optional[str] = ..., createdBy: Optional[int] = ..., updatedBy: Optional[int] = ..., user: Optional[Union[_common_pb2.User, Mapping]] = ..., assistantProviderModelId: Optional[int] = ..., assistantConversactionMessage: Optional[Iterable[Union[AssistantConversactionMessage, Mapping]]] = ..., createdDate: Optional[Union[_timestamp_pb2.Timestamp, Mapping]] = ..., updatedDate: Optional[Union[_timestamp_pb2.Timestamp, Mapping]] = ...) -> None: ...

class AssistantConversactionMessage(_message.Message):
    __slots__ = ["assistantConversactionId", "createdBy", "createdDate", "externalAuditId", "id", "metrics", "request", "requestRole", "response", "responseRole", "source", "stages", "status", "suggestedQuestions", "updatedBy", "updatedDate"]
    ASSISTANTCONVERSACTIONID_FIELD_NUMBER: ClassVar[int]
    CREATEDBY_FIELD_NUMBER: ClassVar[int]
    CREATEDDATE_FIELD_NUMBER: ClassVar[int]
    EXTERNALAUDITID_FIELD_NUMBER: ClassVar[int]
    ID_FIELD_NUMBER: ClassVar[int]
    METRICS_FIELD_NUMBER: ClassVar[int]
    REQUESTROLE_FIELD_NUMBER: ClassVar[int]
    REQUEST_FIELD_NUMBER: ClassVar[int]
    RESPONSEROLE_FIELD_NUMBER: ClassVar[int]
    RESPONSE_FIELD_NUMBER: ClassVar[int]
    SOURCE_FIELD_NUMBER: ClassVar[int]
    STAGES_FIELD_NUMBER: ClassVar[int]
    STATUS_FIELD_NUMBER: ClassVar[int]
    SUGGESTEDQUESTIONS_FIELD_NUMBER: ClassVar[int]
    UPDATEDBY_FIELD_NUMBER: ClassVar[int]
    UPDATEDDATE_FIELD_NUMBER: ClassVar[int]
    assistantConversactionId: int
    createdBy: int
    createdDate: _timestamp_pb2.Timestamp
    externalAuditId: int
    id: int
    metrics: _containers.RepeatedCompositeFieldContainer[_common_pb2.Metric]
    request: _common_pb2.Message
    requestRole: str
    response: _common_pb2.Message
    responseRole: str
    source: str
    stages: _containers.RepeatedCompositeFieldContainer[AssistantMessageStage]
    status: str
    suggestedQuestions: _containers.RepeatedScalarFieldContainer[str]
    updatedBy: int
    updatedDate: _timestamp_pb2.Timestamp
    def __init__(self, id: Optional[int] = ..., assistantConversactionId: Optional[int] = ..., requestRole: Optional[str] = ..., request: Optional[Union[_common_pb2.Message, Mapping]] = ..., responseRole: Optional[str] = ..., response: Optional[Union[_common_pb2.Message, Mapping]] = ..., externalAuditId: Optional[int] = ..., source: Optional[str] = ..., metrics: Optional[Iterable[Union[_common_pb2.Metric, Mapping]]] = ..., status: Optional[str] = ..., createdBy: Optional[int] = ..., updatedBy: Optional[int] = ..., suggestedQuestions: Optional[Iterable[str]] = ..., stages: Optional[Iterable[Union[AssistantMessageStage, Mapping]]] = ..., createdDate: Optional[Union[_timestamp_pb2.Timestamp, Mapping]] = ..., updatedDate: Optional[Union[_timestamp_pb2.Timestamp, Mapping]] = ...) -> None: ...

class AssistantMessageStage(_message.Message):
    __slots__ = ["additionalData", "stage", "timetaken"]
    class AdditionalDataEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: ClassVar[int]
        VALUE_FIELD_NUMBER: ClassVar[int]
        key: str
        value: str
        def __init__(self, key: Optional[str] = ..., value: Optional[str] = ...) -> None: ...
    ADDITIONALDATA_FIELD_NUMBER: ClassVar[int]
    STAGE_FIELD_NUMBER: ClassVar[int]
    TIMETAKEN_FIELD_NUMBER: ClassVar[int]
    additionalData: _containers.ScalarMap[str, str]
    stage: RAGStage
    timetaken: int
    def __init__(self, stage: Optional[Union[RAGStage, str]] = ..., additionalData: Optional[Mapping[str, str]] = ..., timetaken: Optional[int] = ...) -> None: ...

class CreateAssistantMessageRequest(_message.Message):
    __slots__ = ["assistantConversactionId", "assistantId", "assistantProviderModelId", "message"]
    ASSISTANTCONVERSACTIONID_FIELD_NUMBER: ClassVar[int]
    ASSISTANTID_FIELD_NUMBER: ClassVar[int]
    ASSISTANTPROVIDERMODELID_FIELD_NUMBER: ClassVar[int]
    MESSAGE_FIELD_NUMBER: ClassVar[int]
    assistantConversactionId: int
    assistantId: int
    assistantProviderModelId: int
    message: _common_pb2.Message
    def __init__(self, assistantId: Optional[int] = ..., assistantProviderModelId: Optional[int] = ..., message: Optional[Union[_common_pb2.Message, Mapping]] = ..., assistantConversactionId: Optional[int] = ...) -> None: ...

class CreateAssistantMessageResponse(_message.Message):
    __slots__ = ["code", "data", "error", "success"]
    CODE_FIELD_NUMBER: ClassVar[int]
    DATA_FIELD_NUMBER: ClassVar[int]
    ERROR_FIELD_NUMBER: ClassVar[int]
    SUCCESS_FIELD_NUMBER: ClassVar[int]
    code: int
    data: AssistantConversactionMessage
    error: _common_pb2.Error
    success: bool
    def __init__(self, code: Optional[int] = ..., success: bool = ..., data: Optional[Union[AssistantConversactionMessage, Mapping]] = ..., error: Optional[Union[_common_pb2.Error, Mapping]] = ...) -> None: ...

class GetAllAssistantConversactionRequest(_message.Message):
    __slots__ = ["assistantId", "criterias", "paginate"]
    ASSISTANTID_FIELD_NUMBER: ClassVar[int]
    CRITERIAS_FIELD_NUMBER: ClassVar[int]
    PAGINATE_FIELD_NUMBER: ClassVar[int]
    assistantId: int
    criterias: _containers.RepeatedCompositeFieldContainer[_common_pb2.Criteria]
    paginate: _common_pb2.Paginate
    def __init__(self, assistantId: Optional[int] = ..., paginate: Optional[Union[_common_pb2.Paginate, Mapping]] = ..., criterias: Optional[Iterable[Union[_common_pb2.Criteria, Mapping]]] = ...) -> None: ...

class GetAllAssistantConversactionResponse(_message.Message):
    __slots__ = ["code", "data", "error", "paginated", "success"]
    CODE_FIELD_NUMBER: ClassVar[int]
    DATA_FIELD_NUMBER: ClassVar[int]
    ERROR_FIELD_NUMBER: ClassVar[int]
    PAGINATED_FIELD_NUMBER: ClassVar[int]
    SUCCESS_FIELD_NUMBER: ClassVar[int]
    code: int
    data: _containers.RepeatedCompositeFieldContainer[AssistantConversaction]
    error: _common_pb2.Error
    paginated: _common_pb2.Paginated
    success: bool
    def __init__(self, code: Optional[int] = ..., success: bool = ..., data: Optional[Iterable[Union[AssistantConversaction, Mapping]]] = ..., error: Optional[Union[_common_pb2.Error, Mapping]] = ..., paginated: Optional[Union[_common_pb2.Paginated, Mapping]] = ...) -> None: ...

class GetAllConversactionMessageRequest(_message.Message):
    __slots__ = ["assistantConversactionId", "assistantId", "criterias", "order", "paginate"]
    ASSISTANTCONVERSACTIONID_FIELD_NUMBER: ClassVar[int]
    ASSISTANTID_FIELD_NUMBER: ClassVar[int]
    CRITERIAS_FIELD_NUMBER: ClassVar[int]
    ORDER_FIELD_NUMBER: ClassVar[int]
    PAGINATE_FIELD_NUMBER: ClassVar[int]
    assistantConversactionId: int
    assistantId: int
    criterias: _containers.RepeatedCompositeFieldContainer[_common_pb2.Criteria]
    order: _common_pb2.Ordering
    paginate: _common_pb2.Paginate
    def __init__(self, assistantId: Optional[int] = ..., assistantConversactionId: Optional[int] = ..., paginate: Optional[Union[_common_pb2.Paginate, Mapping]] = ..., criterias: Optional[Iterable[Union[_common_pb2.Criteria, Mapping]]] = ..., order: Optional[Union[_common_pb2.Ordering, Mapping]] = ...) -> None: ...

class GetAllConversactionMessageResponse(_message.Message):
    __slots__ = ["code", "data", "error", "paginated", "success"]
    CODE_FIELD_NUMBER: ClassVar[int]
    DATA_FIELD_NUMBER: ClassVar[int]
    ERROR_FIELD_NUMBER: ClassVar[int]
    PAGINATED_FIELD_NUMBER: ClassVar[int]
    SUCCESS_FIELD_NUMBER: ClassVar[int]
    code: int
    data: _containers.RepeatedCompositeFieldContainer[AssistantConversactionMessage]
    error: _common_pb2.Error
    paginated: _common_pb2.Paginated
    success: bool
    def __init__(self, code: Optional[int] = ..., success: bool = ..., data: Optional[Iterable[Union[AssistantConversactionMessage, Mapping]]] = ..., error: Optional[Union[_common_pb2.Error, Mapping]] = ..., paginated: Optional[Union[_common_pb2.Paginated, Mapping]] = ...) -> None: ...

class RAGStage(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
