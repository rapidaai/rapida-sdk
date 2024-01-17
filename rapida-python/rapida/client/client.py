import os

from rapida.api_resources.deployments import RapidaData
from rapida.client.rapida_bridge import RapidaBridge
from rapida.client_options import RapidaClientOptions
from rapida.exceptions.exceptions import RapidaConfigurationException


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
            raise RapidaConfigurationException("The provided API key is invalid.")

        if endpoint_url is None or len(endpoint_url) == 0:
            raise RapidaConfigurationException("The provided endpoint URL is invalid.")

        self.rapida_instances = RapidaData(options=options, rapida_bridge=RapidaBridge(
            service_url=endpoint_url, rapida_api_key=options.rapida_api_key, rapida_region=options.rapida_region, rapida_environment=options.rapida_environment))


