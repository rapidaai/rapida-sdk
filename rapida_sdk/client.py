import os

from rapida_sdk.exceptions import RapidaInvalidAPIException

from .api_resources.deployments import Deployments
from .options import RapidaClientOptions


class Rapida:
    """
    Represents an Rapida client.

    Args:
        options (RapidaClientOptions): The options for the Rapida client.

    Attributes:
        deployments (Deployments): An instance of the Deployments class.

    Raises:
        RapidaInvalidAPIException: If the provided API key is invalid.
    """

    def __init__(self, options: RapidaClientOptions):
        api_key = options.api_key or os.environ.get("RAPIDA_API_KEY")

        if api_key is None or len(api_key) == 0:
            raise RapidaInvalidAPIException("The provided API key is invalid.")

        self.deployments = Deployments(options=options)
