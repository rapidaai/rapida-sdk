import json
import logging
import warnings
from typing import Dict, Mapping, List
from google.protobuf.json_format import MessageToDict, MessageToJson, ParseDict
from google.protobuf.struct_pb2 import Struct

from rapida.artifacts.protos import (
    invoker_api_pb2, common_pb2,
)
from rapida.exceptions import RapidaWarning

_log = logging.getLogger("rapida.exceptions")


class Content:
    _original: common_pb2.Content
    content: bytes
    contentFormat: str
    contentType: str
    meta: Struct

    def __init__(self, data: common_pb2.Content) -> None:
        self.content = data.content
        self.contentFormat = data.contentFormat
        self.contentType = data.contentType
        self.meta = data.meta
        self._original = data

    def to_text(self) -> str:
        if self.contentType == "text" and self.contentFormat == "raw":
            return str(self.content, 'utf-8')
        warnings.warn("to_text should always get called for text format content")

    def to_json(self) -> json:
        return MessageToJson(self._original)

    def to_dict(self) -> Dict:
        return MessageToDict(self._original)


class Metric:
    _original: common_pb2.Metric
    description: str
    name: str
    value: str

    def __init__(self, data: common_pb2.Metric) -> None:
        self.value = data.value
        self.name = data.name
        self.description = data.description
        self._original = data

    def to_json(self) -> json:
        return MessageToJson(self._original)

    def to_dict(self) -> Dict:
        return MessageToDict(self._original)


class InvokeResponseWrapper:
    data: invoker_api_pb2.CallerResponse
    success: bool
    code: int
    error: invoker_api_pb2.InvokerError

    def __init__(self, data: invoker_api_pb2.InvokeResponse) -> None:
        self.code = data.code
        self.success = data.success
        self.data = data.data
        self.error = data.error

    def get_time_taken(self) -> int:
        if self.data.timeTaken is None:
            return 0
        return self.data.timeTaken

    def request_id(self) -> int:
        return self.data.requestId

    def to_json(self) -> json:
        return MessageToJson(self.data)

    def to_dict(self) -> Dict:
        return MessageToDict(self.data)

    def get_data(self) -> List[Content]:
        content_list: List[Content] = []
        for cnt in self.data.responses:
            content_list.append(Content(cnt))
        return content_list

    def get_metrics(self) -> List[Metric]:
        m_list: List[Metric] = []
        for mtr in self.data.metrics:
            m_list.append(Metric(mtr))
        return m_list

    def get_code(self):
        return self.code

    def is_success(self) -> bool:
        return self.success

    def is_error(self) -> bool:
        return not self.is_success()

    def get_error_code(self) -> int:
        if self.error:
            return self.error.errorCode
        else:
            return 0

    def get_error(self) -> Mapping[str, str]:
        if self.error is not None:
            error: Mapping[str, str] = {
                "errorCode": str(self.error.errorCode),
                "errorMessage": self.error.errorMessage,
                "humanMessage": self.error.humanMessage,
            }
            return error
        else:
            _log.warning(RapidaWarning(message="No error message found in response"))
            return {"errorCode": "", "errorMessage": "", "humanMessage": ""}

    def get_error_message(self) -> str:
        if self.error:
            return self.error.errorMessage
        else:
            message = "No error message found in response"
            _log.warning(RapidaWarning(message=message))
        return message

    def get_human_error_message(self) -> str:
        if self.error:
            return self.error.humanMessage
        else:
            _log.warning(RapidaWarning(message="No error message found in response"))
            return "No human error message found in response"
