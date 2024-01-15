import os

from rapida.exceptions.exceptions import RapidaInvalidAPIException, RapidaConfigurationException

from rapida.api_resources.deployments import RapidaData
from rapida.options import RapidaClientOptions


class Rapida:
    """
    Represents an RapidaAI client.

    Args:
        options (RapidaClientOptions): The options for the RapidaAI client.

    Attributes:
        deployments (Deployments): An instance of the Deployments class.

    Raises:
        RapidaInvalidAPIException: If the provided API key is invalid.
    """

    def __init__(self, options: RapidaClientOptions):


        api_key = options.rapida_api_key or os.environ.get("RAPIDA_API_KEY")
        endpoint_url = options.rapida_endpoint_url or os.environ.get("RAPIDA_ENDPOINT_URL")

        if api_key is None or len(api_key) == 0:
            raise RapidaInvalidAPIException("The provided API key is invalid.")

        if endpoint_url is None or len(endpoint_url) == 0:
            raise RapidaConfigurationException("The provided endpoint URL is invalid.")

        self.rapida_instances = RapidaData(options=options)