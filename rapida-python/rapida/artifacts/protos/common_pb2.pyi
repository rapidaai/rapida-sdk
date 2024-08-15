from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Criteria(_message.Message):
    __slots__ = ("key", "value", "logic")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    LOGIC_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: str
    logic: str
    def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ..., logic: _Optional[str] = ...) -> None: ...

class Error(_message.Message):
    __slots__ = ("errorCode", "errorMessage", "humanMessage")
    ERRORCODE_FIELD_NUMBER: _ClassVar[int]
    ERRORMESSAGE_FIELD_NUMBER: _ClassVar[int]
    HUMANMESSAGE_FIELD_NUMBER: _ClassVar[int]
    errorCode: int
    errorMessage: str
    humanMessage: str
    def __init__(self, errorCode: _Optional[int] = ..., errorMessage: _Optional[str] = ..., humanMessage: _Optional[str] = ...) -> None: ...

class Paginate(_message.Message):
    __slots__ = ("page", "pageSize")
    PAGE_FIELD_NUMBER: _ClassVar[int]
    PAGESIZE_FIELD_NUMBER: _ClassVar[int]
    page: int
    pageSize: int
    def __init__(self, page: _Optional[int] = ..., pageSize: _Optional[int] = ...) -> None: ...

class Paginated(_message.Message):
    __slots__ = ("currentPage", "totalItem")
    CURRENTPAGE_FIELD_NUMBER: _ClassVar[int]
    TOTALITEM_FIELD_NUMBER: _ClassVar[int]
    currentPage: int
    totalItem: int
    def __init__(self, currentPage: _Optional[int] = ..., totalItem: _Optional[int] = ...) -> None: ...

class Ordering(_message.Message):
    __slots__ = ("column", "order")
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    column: str
    order: str
    def __init__(self, column: _Optional[str] = ..., order: _Optional[str] = ...) -> None: ...

class User(_message.Message):
    __slots__ = ("id", "name", "email", "role", "createdDate", "status")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    CREATEDDATE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    email: str
    role: str
    createdDate: _timestamp_pb2.Timestamp
    status: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., email: _Optional[str] = ..., role: _Optional[str] = ..., createdDate: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., status: _Optional[str] = ...) -> None: ...

class BaseResponse(_message.Message):
    __slots__ = ("code", "success", "data", "error")
    class DataEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    CODE_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    code: int
    success: bool
    data: _containers.ScalarMap[str, str]
    error: Error
    def __init__(self, code: _Optional[int] = ..., success: bool = ..., data: _Optional[_Mapping[str, str]] = ..., error: _Optional[_Union[Error, _Mapping]] = ...) -> None: ...

class Metadata(_message.Message):
    __slots__ = ("id", "key", "value")
    ID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    id: int
    key: str
    value: str
    def __init__(self, id: _Optional[int] = ..., key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...

class Variable(_message.Message):
    __slots__ = ("id", "name", "type", "defaultValue", "required", "label")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DEFAULTVALUE_FIELD_NUMBER: _ClassVar[int]
    IN_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    type: str
    defaultValue: str
    required: bool
    label: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., type: _Optional[str] = ..., defaultValue: _Optional[str] = ..., required: bool = ..., label: _Optional[str] = ..., **kwargs) -> None: ...

class ProviderModelParameter(_message.Message):
    __slots__ = ("id", "providerModelVariableId", "value")
    ID_FIELD_NUMBER: _ClassVar[int]
    PROVIDERMODELVARIABLEID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    id: int
    providerModelVariableId: int
    value: str
    def __init__(self, id: _Optional[int] = ..., providerModelVariableId: _Optional[int] = ..., value: _Optional[str] = ...) -> None: ...

class Provider(_message.Message):
    __slots__ = ("id", "name", "description", "humanName", "image", "website", "status", "connectConfiguration")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    HUMANNAME_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    WEBSITE_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CONNECTCONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    description: str
    humanName: str
    image: str
    website: str
    status: str
    connectConfiguration: _containers.RepeatedCompositeFieldContainer[Variable]
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., humanName: _Optional[str] = ..., image: _Optional[str] = ..., website: _Optional[str] = ..., status: _Optional[str] = ..., connectConfiguration: _Optional[_Iterable[_Union[Variable, _Mapping]]] = ...) -> None: ...

class ProviderModelVariable(_message.Message):
    __slots__ = ("id", "providerModelId", "key", "name", "description", "defaultValue", "type", "place", "metadatas")
    ID_FIELD_NUMBER: _ClassVar[int]
    PROVIDERMODELID_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DEFAULTVALUE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PLACE_FIELD_NUMBER: _ClassVar[int]
    METADATAS_FIELD_NUMBER: _ClassVar[int]
    id: int
    providerModelId: int
    key: str
    name: str
    description: str
    defaultValue: str
    type: str
    place: str
    metadatas: _containers.RepeatedCompositeFieldContainer[Metadata]
    def __init__(self, id: _Optional[int] = ..., providerModelId: _Optional[int] = ..., key: _Optional[str] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., defaultValue: _Optional[str] = ..., type: _Optional[str] = ..., place: _Optional[str] = ..., metadatas: _Optional[_Iterable[_Union[Metadata, _Mapping]]] = ...) -> None: ...

class ModelEndpoint(_message.Message):
    __slots__ = ("endpoint",)
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    endpoint: str
    def __init__(self, endpoint: _Optional[str] = ...) -> None: ...

class ProviderModel(_message.Message):
    __slots__ = ("id", "name", "description", "humanName", "category", "status", "owner", "provider", "parameters", "metadatas", "providerId", "endpoints")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    HUMANNAME_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    PROVIDER_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    METADATAS_FIELD_NUMBER: _ClassVar[int]
    PROVIDERID_FIELD_NUMBER: _ClassVar[int]
    ENDPOINTS_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    description: str
    humanName: str
    category: str
    status: str
    owner: str
    provider: Provider
    parameters: _containers.RepeatedCompositeFieldContainer[ProviderModelVariable]
    metadatas: _containers.RepeatedCompositeFieldContainer[Metadata]
    providerId: int
    endpoints: _containers.RepeatedCompositeFieldContainer[ModelEndpoint]
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., humanName: _Optional[str] = ..., category: _Optional[str] = ..., status: _Optional[str] = ..., owner: _Optional[str] = ..., provider: _Optional[_Union[Provider, _Mapping]] = ..., parameters: _Optional[_Iterable[_Union[ProviderModelVariable, _Mapping]]] = ..., metadatas: _Optional[_Iterable[_Union[Metadata, _Mapping]]] = ..., providerId: _Optional[int] = ..., endpoints: _Optional[_Iterable[_Union[ModelEndpoint, _Mapping]]] = ...) -> None: ...

class Tag(_message.Message):
    __slots__ = ("id", "tag")
    ID_FIELD_NUMBER: _ClassVar[int]
    TAG_FIELD_NUMBER: _ClassVar[int]
    id: int
    tag: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[int] = ..., tag: _Optional[_Iterable[str]] = ...) -> None: ...

class Organization(_message.Message):
    __slots__ = ("id", "name", "description", "industry", "contact", "size")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    INDUSTRY_FIELD_NUMBER: _ClassVar[int]
    CONTACT_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    description: str
    industry: str
    contact: str
    size: str
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., industry: _Optional[str] = ..., contact: _Optional[str] = ..., size: _Optional[str] = ...) -> None: ...

class Metric(_message.Message):
    __slots__ = ("name", "value", "description")
    NAME_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    value: str
    description: str
    def __init__(self, name: _Optional[str] = ..., value: _Optional[str] = ..., description: _Optional[str] = ...) -> None: ...

class Content(_message.Message):
    __slots__ = ("name", "contentType", "contentFormat", "content", "meta")
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONTENTTYPE_FIELD_NUMBER: _ClassVar[int]
    CONTENTFORMAT_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    META_FIELD_NUMBER: _ClassVar[int]
    name: str
    contentType: str
    contentFormat: str
    content: bytes
    meta: _struct_pb2.Struct
    def __init__(self, name: _Optional[str] = ..., contentType: _Optional[str] = ..., contentFormat: _Optional[str] = ..., content: _Optional[bytes] = ..., meta: _Optional[_Union[_struct_pb2.Struct, _Mapping]] = ...) -> None: ...

class Message(_message.Message):
    __slots__ = ("role", "contents")
    ROLE_FIELD_NUMBER: _ClassVar[int]
    CONTENTS_FIELD_NUMBER: _ClassVar[int]
    role: str
    contents: _containers.RepeatedCompositeFieldContainer[Content]
    def __init__(self, role: _Optional[str] = ..., contents: _Optional[_Iterable[_Union[Content, _Mapping]]] = ...) -> None: ...

class Knowledge(_message.Message):
    __slots__ = ("id", "name", "description", "visibility", "language", "embeddingProviderModelId", "embeddingProviderModel", "status", "createdBy", "createdUser", "updatedBy", "updatedUser", "createdDate", "updatedDate", "organizationId", "projectId", "organization", "knowledgeTag", "documentCount", "tokenCount", "wordCount", "embeddingProviderId")
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    VISIBILITY_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    EMBEDDINGPROVIDERMODELID_FIELD_NUMBER: _ClassVar[int]
    EMBEDDINGPROVIDERMODEL_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    CREATEDBY_FIELD_NUMBER: _ClassVar[int]
    CREATEDUSER_FIELD_NUMBER: _ClassVar[int]
    UPDATEDBY_FIELD_NUMBER: _ClassVar[int]
    UPDATEDUSER_FIELD_NUMBER: _ClassVar[int]
    CREATEDDATE_FIELD_NUMBER: _ClassVar[int]
    UPDATEDDATE_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATIONID_FIELD_NUMBER: _ClassVar[int]
    PROJECTID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_FIELD_NUMBER: _ClassVar[int]
    KNOWLEDGETAG_FIELD_NUMBER: _ClassVar[int]
    DOCUMENTCOUNT_FIELD_NUMBER: _ClassVar[int]
    TOKENCOUNT_FIELD_NUMBER: _ClassVar[int]
    WORDCOUNT_FIELD_NUMBER: _ClassVar[int]
    EMBEDDINGPROVIDERID_FIELD_NUMBER: _ClassVar[int]
    id: int
    name: str
    description: str
    visibility: str
    language: str
    embeddingProviderModelId: int
    embeddingProviderModel: ProviderModel
    status: str
    createdBy: int
    createdUser: User
    updatedBy: int
    updatedUser: User
    createdDate: _timestamp_pb2.Timestamp
    updatedDate: _timestamp_pb2.Timestamp
    organizationId: int
    projectId: int
    organization: Organization
    knowledgeTag: Tag
    documentCount: int
    tokenCount: int
    wordCount: int
    embeddingProviderId: int
    def __init__(self, id: _Optional[int] = ..., name: _Optional[str] = ..., description: _Optional[str] = ..., visibility: _Optional[str] = ..., language: _Optional[str] = ..., embeddingProviderModelId: _Optional[int] = ..., embeddingProviderModel: _Optional[_Union[ProviderModel, _Mapping]] = ..., status: _Optional[str] = ..., createdBy: _Optional[int] = ..., createdUser: _Optional[_Union[User, _Mapping]] = ..., updatedBy: _Optional[int] = ..., updatedUser: _Optional[_Union[User, _Mapping]] = ..., createdDate: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., updatedDate: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., organizationId: _Optional[int] = ..., projectId: _Optional[int] = ..., organization: _Optional[_Union[Organization, _Mapping]] = ..., knowledgeTag: _Optional[_Union[Tag, _Mapping]] = ..., documentCount: _Optional[int] = ..., tokenCount: _Optional[int] = ..., wordCount: _Optional[int] = ..., embeddingProviderId: _Optional[int] = ...) -> None: ...
