#  Copyright (c) 2024. Rapida
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#  THE SOFTWARE.
#
#  Author: Prashant <prashant@rapida.ai>

import json
import logging
from os import name
import warnings
from typing import Dict, Mapping, List, MutableMapping
from google.protobuf.json_format import MessageToDict, MessageToJson
from google.protobuf.struct_pb2 import Struct
from pydantic import BaseModel

from rapida.artifacts.protos import (
    integration_api_pb2,
    invoker_api_pb2,
    common_pb2,
)
from rapida.exceptions import RapidaWarning

_log = logging.getLogger("rapida.client")


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
            return str(self.content, "utf-8")
        warnings.warn("to_text should always get called for text format content")

    def to_json(self) -> json:
        return MessageToJson(self._original)

    def to_dict(self) -> Dict:
        return MessageToDict(self._original)

    @staticmethod
    def from_text(cntnt: str) -> common_pb2.Content:
        return common_pb2.Content(
            contentType="text",
            contentFormat="raw",
            content=cntnt.encode("utf-8"),
        )


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

    def get_metadata(self) -> Dict:
        return MessageToDict(self.data.meta)

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


class Message:
    role: str
    contents: List[common_pb2.Content]

    def __init__(self, role: str, contents: List[common_pb2.Content]):
        self.role = role
        self.contents = contents

    def to_message(self) -> common_pb2.Message:
        return common_pb2.Message(role=self.role, contents=self.contents)

    @staticmethod
    def from_text(role: str, content: str) -> "Message":
        return Message(role=role, contents=[Content.from_text(content)])


class FunctionParameterProperty:
    def __init__(self, type: str, description: str):
        self.type = type
        self.description = description

    def to_function_parameter_property(
        self,
    ) -> integration_api_pb2.FunctionParameterProperty:
        return integration_api_pb2.FunctionParameterProperty(
            type=self.type, description=self.description
        )


class FunctionParameter:
    def __init__(
        self,
        required: List[str],
        type: str,
        properties: Mapping[str, FunctionParameterProperty],
    ):
        self.required = required
        self.type = type
        self.properties = properties

    def to_function_parameter(self) -> integration_api_pb2.FunctionParameter:
        _map: Dict[str, integration_api_pb2.FunctionParameterProperty] = {}
        for k, v in self.properties.items():
            _map[k] = v.to_function_parameter_property()
        return integration_api_pb2.FunctionParameter(
            required=self.required,
            type=self.type,
            properties=_map,
        )


class FunctionDefinition:
    def __init__(self, name: str, description: str, parameters: FunctionParameter):
        self.name = name
        self.description = description
        self.parameters = parameters

    def to_function_definition(self) -> integration_api_pb2.FunctionDefinition:
        return integration_api_pb2.FunctionDefinition(
            name=self.name,
            description=self.description,
            parameters=self.parameters.to_function_parameter(),
        )

    @classmethod
    def from_dict(cls, data: dict) -> "FunctionDefinition":
        parameters_data = data["parameters"]
        properties = {
            k: FunctionParameterProperty(type=v["type"], description=v["description"])
            for k, v in parameters_data["properties"].items()
        }
        parameters = FunctionParameter(
            required=parameters_data["required"],
            type=parameters_data["type"],
            properties=properties,
        )
        return cls(
            name=data["name"], description=data["description"], parameters=parameters
        )


class ToolDefinition:
    def __init__(self, type: str, function_definition: FunctionDefinition):
        self.type = type
        self.function_definition = function_definition

    def to_tool_definition(self) -> integration_api_pb2.ToolDefinition:
        return integration_api_pb2.ToolDefinition(
            type=self.type,
            functionDefinition=self.function_definition.to_function_definition(),  # Call the method here
        )

    @classmethod
    def from_function(cls, fc: Dict) -> "ToolDefinition":
        return ToolDefinition(
            type="function", function_definition=FunctionDefinition.from_dict(fc)
        )
