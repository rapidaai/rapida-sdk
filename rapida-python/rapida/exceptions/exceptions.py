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

import logging
from rapida.artifacts.protos.invoker_api_pb2 import InvokerError

_log = logging.getLogger("rapida.exceptions")


class RapidaException(Exception):
    """Exception raised for errors when interacting with deployments.

    Attributes:
        code (int): The error code returned by the API
        message (str): The error message returned by the API
        source (str): The source of the error. If the source is
        `provider`, the error is raised by the model provider.
    """

    def __init__(self, code: int, message: str, source: str):
        """
        Initialize a new instance of the Exception class.

        Args:
            code (str): The error code.
            message (str): The error message.
            source (str): The source of the error.

        """
        self.code = code
        self.message = message
        self.source = source
        super().__init__(self.message)

    def __str__(self) -> str:
        """
        Returns a string representation of the exception.

        Returns:
            str: The formatted string representation of the exception.
        """
        return f"[{self.source}] - [code:{self.code}]: {self.message}"


class RapidaConfigurationException(RapidaException):
    """
    An error caused by client or server configuration
    """

    def __init__(self, message: str, source: str):
        super().__init__(400, message, source)


class RapidaInternalServerException(RapidaException):
    """An error caused by uncontrolled server response"""

    def __init__(self, code: int, message: str, source: str):
        super().__init__(code, message, source)


class RapidaInvalidAPIException(RapidaException):
    """Raised if the provider API key is invalid."""

    def __init__(self, code: int, message: str, source: str):
        super().__init__(code, message, source)


def handle_request_exception(error: InvokerError):
    """

    Args:
        error: error returned by invoker that represent what really went wrong.

    Returns: an instance of exception class

    """
    try:
        # error_json = response.json()
        raise RapidaException(
            code=error.errorCode,
            message=error.humanMessage,
            source=error.errorMessage,
        )
    except ValueError:
        raise RapidaException(
            code=500,
            message="An unknown error occurred.",
            source="unknown",
        )


class RapidaWarning(Warning):
    """
    Warning message
    """

    message: str

    def __init__(self, message: str):
        super().__init__(message)

    def __str__(self) -> str:
        """
        Returns a string representation of the exception.

        Returns:
            str: The formatted string representation of the exception.
        """
        return f"[{self.message}"
