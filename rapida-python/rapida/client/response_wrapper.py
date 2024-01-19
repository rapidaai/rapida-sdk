import json
import logging
from typing import Mapping

from rapida.artifacts.protos.endpoint_service import (
    invoker_api_pb2,
)
from rapida.exceptions import RapidaWarning

_log = logging.getLogger("rapida.exceptions")


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

    def to_json(self) -> json:
        rsp: json = json.loads(self.data.response)
        return rsp

    def to_dict(self) -> Mapping[str, str]:
        results: Mapping[str, str] = []
        for _k, _v in self.get_json_response(self.data.response):
            results[_k] = _v
        return results

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
