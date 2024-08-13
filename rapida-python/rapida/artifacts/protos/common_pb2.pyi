from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar, Iterable, Mapping, Optional, Union

DESCRIPTOR: _descriptor.FileDescriptor

class BaseResponse(_message.Message):
    __slots__ = ["code", "data", "error", "success"]
    class DataEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: ClassVar[int]
        VALUE_FIELD_NUMBER: ClassVar[int]
        key: str
        value: str
        def __init__(self, key: Optional[str] = ..., value: Optional[str] = ...) -> None: ...
    CODE_FIELD_NUMBER: ClassVar[int]
    DATA_FIELD_NUMBER: ClassVar[int]
    ERROR_FIELD_NUMBER: ClassVar[int]
    SUCCESS_FIELD_NUMBER: ClassVar[int]
    code: int
    data: _containers.ScalarMap[str, str]
    error: Error
    success: bool
    def __init__(self, code: Optional[int] = ..., success: bool = ..., data: Optional[Mapping[str, str]] = ..., error: Optional[Union[Error, Mapping]] = ...) -> None: ...

class Content(_message.Message):
    __slots__ = ["content", "contentFormat", "contentType", "meta", "name"]
    CONTENTFORMAT_FIELD_NUMBER: ClassVar[int]
    CONTENTTYPE_FIELD_NUMBER: ClassVar[int]
    CONTENT_FIELD_NUMBER: ClassVar[int]
    META_FIELD_NUMBER: ClassVar[int]
    NAME_FIELD_NUMBER: ClassVar[int]
    content: bytes
    contentFormat: str
    contentType: str
    meta: _struct_pb2.Struct
    name: str
    def __init__(self, name: Optional[str] = ..., contentType: Optional[str] = ..., contentFormat: Optional[str] = ..., content: Optional[bytes] = ..., meta: Optional[Union[_struct_pb2.Struct, Mapping]] = ...) -> None: ...

class Criteria(_message.Message):
    __slots__ = ["key", "logic", "value"]
    KEY_FIELD_NUMBER: ClassVar[int]
    LOGIC_FIELD_NUMBER: ClassVar[int]
    VALUE_FIELD_NUMBER: ClassVar[int]
    key: str
    logic: str
    value: str
    def __init__(self, key: Optional[str] = ..., value: Optional[str] = ..., logic: Optional[str] = ...) -> None: ...

class Error(_message.Message):
    __slots__ = ["errorCode", "errorMessage", "humanMessage"]
    ERRORCODE_FIELD_NUMBER: ClassVar[int]
    ERRORMESSAGE_FIELD_NUMBER: ClassVar[int]
    HUMANMESSAGE_FIELD_NUMBER: ClassVar[int]
    errorCode: int
    errorMessage: str
    humanMessage: str
    def __init__(self, errorCode: Optional[int] = ..., errorMessage: Optional[str] = ..., humanMessage: Optional[str] = ...) -> None: ...

class Knowledge(_message.Message):
    __slots__ = ["createdBy", "createdDate", "createdUser", "description", "documentCount", "embeddingProviderId", "embeddingProviderModel", "embeddingProviderModelId", "id", "knowledgeTag", "language", "name", "organization", "organizationId", "projectId", "status", "tokenCount", "updatedBy", "updatedDate", "updatedUser", "visibility", "wordCount"]
    CREATEDBY_FIELD_NUMBER: ClassVar[int]
    CREATEDDATE_FIELD_NUMBER: ClassVar[int]
    CREATEDUSER_FIELD_NUMBER: ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: ClassVar[int]
    DOCUMENTCOUNT_FIELD_NUMBER: ClassVar[int]
    EMBEDDINGPROVIDERID_FIELD_NUMBER: ClassVar[int]
    EMBEDDINGPROVIDERMODELID_FIELD_NUMBER: ClassVar[int]
    EMBEDDINGPROVIDERMODEL_FIELD_NUMBER: ClassVar[int]
    ID_FIELD_NUMBER: ClassVar[int]
    KNOWLEDGETAG_FIELD_NUMBER: ClassVar[int]
    LANGUAGE_FIELD_NUMBER: ClassVar[int]
    NAME_FIELD_NUMBER: ClassVar[int]
    ORGANIZATIONID_FIELD_NUMBER: ClassVar[int]
    ORGANIZATION_FIELD_NUMBER: ClassVar[int]
    PROJECTID_FIELD_NUMBER: ClassVar[int]
    STATUS_FIELD_NUMBER: ClassVar[int]
    TOKENCOUNT_FIELD_NUMBER: ClassVar[int]
    UPDATEDBY_FIELD_NUMBER: ClassVar[int]
    UPDATEDDATE_FIELD_NUMBER: ClassVar[int]
    UPDATEDUSER_FIELD_NUMBER: ClassVar[int]
    VISIBILITY_FIELD_NUMBER: ClassVar[int]
    WORDCOUNT_FIELD_NUMBER: ClassVar[int]
    createdBy: int
    createdDate: _timestamp_pb2.Timestamp
    createdUser: User
    description: str
    documentCount: int
    embeddingProviderId: int
    embeddingProviderModel: ProviderModel
    embeddingProviderModelId: int
    id: int
    knowledgeTag: Tag
    language: str
    name: str
    organization: Organization
    organizationId: int
    projectId: int
    status: str
    tokenCount: int
    updatedBy: int
    updatedDate: _timestamp_pb2.Timestamp
    updatedUser: User
    visibility: str
    wordCount: int
    def __init__(self, id: Optional[int] = ..., name: Optional[str] = ..., description: Optional[str] = ..., visibility: Optional[str] = ..., language: Optional[str] = ..., embeddingProviderModelId: Optional[int] = ..., embeddingProviderModel: Optional[Union[ProviderModel, Mapping]] = ..., status: Optional[str] = ..., createdBy: Optional[int] = ..., createdUser: Optional[Union[User, Mapping]] = ..., updatedBy: Optional[int] = ..., updatedUser: Optional[Union[User, Mapping]] = ..., createdDate: Optional[Union[_timestamp_pb2.Timestamp, Mapping]] = ..., updatedDate: Optional[Union[_timestamp_pb2.Timestamp, Mapping]] = ..., organizationId: Optional[int] = ..., projectId: Optional[int] = ..., organization: Optional[Union[Organization, Mapping]] = ..., knowledgeTag: Optional[Union[Tag, Mapping]] = ..., documentCount: Optional[int] = ..., tokenCount: Optional[int] = ..., wordCount: Optional[int] = ..., embeddingProviderId: Optional[int] = ...) -> None: ...

class Message(_message.Message):
    __slots__ = ["contents", "role"]
    CONTENTS_FIELD_NUMBER: ClassVar[int]
    ROLE_FIELD_NUMBER: ClassVar[int]
    contents: _containers.RepeatedCompositeFieldContainer[Content]
    role: str
    def __init__(self, role: Optional[str] = ..., contents: Optional[Iterable[Union[Content, Mapping]]] = ...) -> None: ...

class Metadata(_message.Message):
    __slots__ = ["id", "key", "value"]
    ID_FIELD_NUMBER: ClassVar[int]
    KEY_FIELD_NUMBER: ClassVar[int]
    VALUE_FIELD_NUMBER: ClassVar[int]
    id: int
    key: str
    value: str
    def __init__(self, id: Optional[int] = ..., key: Optional[str] = ..., value: Optional[str] = ...) -> None: ...

class Metric(_message.Message):
    __slots__ = ["description", "name", "value"]
    DESCRIPTION_FIELD_NUMBER: ClassVar[int]
    NAME_FIELD_NUMBER: ClassVar[int]
    VALUE_FIELD_NUMBER: ClassVar[int]
    description: str
    name: str
    value: str
    def __init__(self, name: Optional[str] = ..., value: Optional[str] = ..., description: Optional[str] = ...) -> None: ...

class ModelEndpoint(_message.Message):
    __slots__ = ["endpoint"]
    ENDPOINT_FIELD_NUMBER: ClassVar[int]
    endpoint: str
    def __init__(self, endpoint: Optional[str] = ...) -> None: ...

class Ordering(_message.Message):
    __slots__ = ["column", "order"]
    COLUMN_FIELD_NUMBER: ClassVar[int]
    ORDER_FIELD_NUMBER: ClassVar[int]
    column: str
    order: str
    def __init__(self, column: Optional[str] = ..., order: Optional[str] = ...) -> None: ...

class Organization(_message.Message):
    __slots__ = ["contact", "description", "id", "industry", "name", "size"]
    CONTACT_FIELD_NUMBER: ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: ClassVar[int]
    ID_FIELD_NUMBER: ClassVar[int]
    INDUSTRY_FIELD_NUMBER: ClassVar[int]
    NAME_FIELD_NUMBER: ClassVar[int]
    SIZE_FIELD_NUMBER: ClassVar[int]
    contact: str
    description: str
    id: int
    industry: str
    name: str
    size: str
    def __init__(self, id: Optional[int] = ..., name: Optional[str] = ..., description: Optional[str] = ..., industry: Optional[str] = ..., contact: Optional[str] = ..., size: Optional[str] = ...) -> None: ...

class Paginate(_message.Message):
    __slots__ = ["page", "pageSize"]
    PAGESIZE_FIELD_NUMBER: ClassVar[int]
    PAGE_FIELD_NUMBER: ClassVar[int]
    page: int
    pageSize: int
    def __init__(self, page: Optional[int] = ..., pageSize: Optional[int] = ...) -> None: ...

class Paginated(_message.Message):
    __slots__ = ["currentPage", "totalItem"]
    CURRENTPAGE_FIELD_NUMBER: ClassVar[int]
    TOTALITEM_FIELD_NUMBER: ClassVar[int]
    currentPage: int
    totalItem: int
    def __init__(self, currentPage: Optional[int] = ..., totalItem: Optional[int] = ...) -> None: ...

class Provider(_message.Message):
    __slots__ = ["connectConfiguration", "description", "humanName", "id", "image", "name", "status", "website"]
    CONNECTCONFIGURATION_FIELD_NUMBER: ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: ClassVar[int]
    HUMANNAME_FIELD_NUMBER: ClassVar[int]
    ID_FIELD_NUMBER: ClassVar[int]
    IMAGE_FIELD_NUMBER: ClassVar[int]
    NAME_FIELD_NUMBER: ClassVar[int]
    STATUS_FIELD_NUMBER: ClassVar[int]
    WEBSITE_FIELD_NUMBER: ClassVar[int]
    connectConfiguration: _containers.RepeatedCompositeFieldContainer[Variable]
    description: str
    humanName: str
    id: int
    image: str
    name: str
    status: str
    website: str
    def __init__(self, id: Optional[int] = ..., name: Optional[str] = ..., description: Optional[str] = ..., humanName: Optional[str] = ..., image: Optional[str] = ..., website: Optional[str] = ..., status: Optional[str] = ..., connectConfiguration: Optional[Iterable[Union[Variable, Mapping]]] = ...) -> None: ...

class ProviderModel(_message.Message):
    __slots__ = ["category", "description", "endpoints", "humanName", "id", "metadatas", "name", "owner", "parameters", "provider", "providerId", "status"]
    CATEGORY_FIELD_NUMBER: ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: ClassVar[int]
    ENDPOINTS_FIELD_NUMBER: ClassVar[int]
    HUMANNAME_FIELD_NUMBER: ClassVar[int]
    ID_FIELD_NUMBER: ClassVar[int]
    METADATAS_FIELD_NUMBER: ClassVar[int]
    NAME_FIELD_NUMBER: ClassVar[int]
    OWNER_FIELD_NUMBER: ClassVar[int]
    PARAMETERS_FIELD_NUMBER: ClassVar[int]
    PROVIDERID_FIELD_NUMBER: ClassVar[int]
    PROVIDER_FIELD_NUMBER: ClassVar[int]
    STATUS_FIELD_NUMBER: ClassVar[int]
    category: str
    description: str
    endpoints: _containers.RepeatedCompositeFieldContainer[ModelEndpoint]
    humanName: str
    id: int
    metadatas: _containers.RepeatedCompositeFieldContainer[Metadata]
    name: str
    owner: str
    parameters: _containers.RepeatedCompositeFieldContainer[ProviderModelVariable]
    provider: Provider
    providerId: int
    status: str
    def __init__(self, id: Optional[int] = ..., name: Optional[str] = ..., description: Optional[str] = ..., humanName: Optional[str] = ..., category: Optional[str] = ..., status: Optional[str] = ..., owner: Optional[str] = ..., provider: Optional[Union[Provider, Mapping]] = ..., parameters: Optional[Iterable[Union[ProviderModelVariable, Mapping]]] = ..., metadatas: Optional[Iterable[Union[Metadata, Mapping]]] = ..., providerId: Optional[int] = ..., endpoints: Optional[Iterable[Union[ModelEndpoint, Mapping]]] = ...) -> None: ...

class ProviderModelParameter(_message.Message):
    __slots__ = ["id", "providerModelVariableId", "value"]
    ID_FIELD_NUMBER: ClassVar[int]
    PROVIDERMODELVARIABLEID_FIELD_NUMBER: ClassVar[int]
    VALUE_FIELD_NUMBER: ClassVar[int]
    id: int
    providerModelVariableId: int
    value: str
    def __init__(self, id: Optional[int] = ..., providerModelVariableId: Optional[int] = ..., value: Optional[str] = ...) -> None: ...

class ProviderModelVariable(_message.Message):
    __slots__ = ["defaultValue", "description", "id", "key", "metadatas", "name", "place", "providerModelId", "type"]
    DEFAULTVALUE_FIELD_NUMBER: ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: ClassVar[int]
    ID_FIELD_NUMBER: ClassVar[int]
    KEY_FIELD_NUMBER: ClassVar[int]
    METADATAS_FIELD_NUMBER: ClassVar[int]
    NAME_FIELD_NUMBER: ClassVar[int]
    PLACE_FIELD_NUMBER: ClassVar[int]
    PROVIDERMODELID_FIELD_NUMBER: ClassVar[int]
    TYPE_FIELD_NUMBER: ClassVar[int]
    defaultValue: str
    description: str
    id: int
    key: str
    metadatas: _containers.RepeatedCompositeFieldContainer[Metadata]
    name: str
    place: str
    providerModelId: int
    type: str
    def __init__(self, id: Optional[int] = ..., providerModelId: Optional[int] = ..., key: Optional[str] = ..., name: Optional[str] = ..., description: Optional[str] = ..., defaultValue: Optional[str] = ..., type: Optional[str] = ..., place: Optional[str] = ..., metadatas: Optional[Iterable[Union[Metadata, Mapping]]] = ...) -> None: ...

class Tag(_message.Message):
    __slots__ = ["id", "tag"]
    ID_FIELD_NUMBER: ClassVar[int]
    TAG_FIELD_NUMBER: ClassVar[int]
    id: int
    tag: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: Optional[int] = ..., tag: Optional[Iterable[str]] = ...) -> None: ...

class User(_message.Message):
    __slots__ = ["createdDate", "email", "id", "name", "role", "status"]
    CREATEDDATE_FIELD_NUMBER: ClassVar[int]
    EMAIL_FIELD_NUMBER: ClassVar[int]
    ID_FIELD_NUMBER: ClassVar[int]
    NAME_FIELD_NUMBER: ClassVar[int]
    ROLE_FIELD_NUMBER: ClassVar[int]
    STATUS_FIELD_NUMBER: ClassVar[int]
    createdDate: _timestamp_pb2.Timestamp
    email: str
    id: int
    name: str
    role: str
    status: str
    def __init__(self, id: Optional[int] = ..., name: Optional[str] = ..., email: Optional[str] = ..., role: Optional[str] = ..., createdDate: Optional[Union[_timestamp_pb2.Timestamp, Mapping]] = ..., status: Optional[str] = ...) -> None: ...

class Variable(_message.Message):
    __slots__ = ["defaultValue", "id", "label", "name", "required", "type"]
    DEFAULTVALUE_FIELD_NUMBER: ClassVar[int]
    ID_FIELD_NUMBER: ClassVar[int]
    IN_FIELD_NUMBER: ClassVar[int]
    LABEL_FIELD_NUMBER: ClassVar[int]
    NAME_FIELD_NUMBER: ClassVar[int]
    REQUIRED_FIELD_NUMBER: ClassVar[int]
    TYPE_FIELD_NUMBER: ClassVar[int]
    defaultValue: str
    id: int
    label: str
    name: str
    required: bool
    type: str
    def __init__(self, id: Optional[int] = ..., name: Optional[str] = ..., type: Optional[str] = ..., defaultValue: Optional[str] = ..., required: bool = ..., label: Optional[str] = ..., **kwargs) -> None: ...
