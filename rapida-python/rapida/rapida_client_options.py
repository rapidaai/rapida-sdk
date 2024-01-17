from typing import Optional, Union
import os


class RapidaClientOptions:
    """
    RapidaAI client options
    """

    rapida_api_key: str
    rapida_endpoint_url: str
    rapida_region: Union["ap", "us", "eu", "any"]
    rapida_environment: Optional[str]

    def __init__(
        self,
        rapida_api_key: Optional[str] = None,
        rapida_endpoint_url: Optional[str] = None,
        rapida_environment: Optional[str] = "production",
        rapida_region: Optional[Union["ap", "us", "eu"]] = "all",
    ):

        """

        Args:
            rapida_api_key:
            rapida_endpoint_url:
            rapida_region:
            rapida_environment:
        """
        self.rapida_api_key = rapida_api_key or os.environ.get("RAPIDA_API_KEY")
        self.rapida_endpoint_url = rapida_endpoint_url or os.environ.get(
            "RAPIDA_ENDPOINT_URL"
        )
        self.rapida_environment = rapida_environment or os.environ.get(
            "RAPIDA_ENVIRONMENT"
        )
        self.rapida_region = rapida_region or os.environ.get("RAPIDA_REGION")
