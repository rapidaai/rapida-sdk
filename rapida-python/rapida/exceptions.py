class RapidaException(Exception):
    """Exception raised for errors when interacting with deployments.

    Attributes:
        code (int): The error code returned by the API
        message (str): The error message returned by the API
        source (str): The source of the error. If the source is `provider`, the error is raised by the model provider.
    """

    def __init__(self, code: str, message: str, source: str):
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

    pass


class RapidaInternalServerException(RapidaException):
    """An error caused by uncontrolled server response"""

    pass


def handle_request_exception(response: Response):
    try:
        error_json = response.json()
        raise RapidaException(
            code=error_json.get("code", None),
            message=error_json.get("error", None),
            source=error_json.get("source", None),
        )
    except ValueError:
        raise RapidaException(
            code="unknown",
            message="An unknown error occurred.",
            source="unknown",
        )
