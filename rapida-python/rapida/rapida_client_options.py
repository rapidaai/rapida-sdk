from typing import Optional, Union
import os
from enum import Enum
import warnings


class RapidaEnvironment(Enum):
    """
    Rapida Environment
    """
    PRODUCTION = "production"
    DEVELOPMENT = "development"

    def get(self) -> str:
        return str(self.value)

    @staticmethod
    def from_str(label):
        if label == "production":
            return RapidaEnvironment.PRODUCTION
        elif label == "development":
            return RapidaEnvironment.DEVELOPMENT
        else:
            warnings.warn("the environment is not supported only use production and development.")
            return RapidaEnvironment.DEVELOPMENT


class RapidaRegion(Enum):
    """
    Region supported by rapida service
    """
    AP = "ap"
    US = "us"
    EU = "eu"
    ALL = "all"

    def get(self) -> str:
        return str(self.value)

    @staticmethod
    def from_str(label):
        if label == "ap":
            return RapidaRegion.AP
        elif label == "us":
            return RapidaRegion.US
        elif label == "eu":
            return RapidaRegion.EU
        else:
            warnings.warn("the region is not support, supported region ap, us, eu and all")
            return RapidaRegion.ALL


class RapidaClientOptions:
    """
    RapidaAI client options
    """

    rapida_api_key: str
    rapida_endpoint_url: str
    rapida_region: Optional[RapidaRegion]
    rapida_environment: Optional[RapidaEnvironment]

    def __init__(
            self,
            api_key: Optional[str] = None,
            endpoint_url: Optional[str] = None,
            environment: Optional[RapidaEnvironment] = RapidaEnvironment.PRODUCTION,
            region: Optional[RapidaRegion] = RapidaRegion.ALL,
    ):
        """

        Args:
            api_key:
            endpoint_url:
            region:
            environment:
        """
        self.rapida_api_key = api_key or os.environ.get("RAPIDA_API_KEY")
        self.rapida_endpoint_url = endpoint_url or os.environ.get(
            "RAPIDA_ENDPOINT_URL"
        )
        self.rapida_environment = environment or os.environ.get(
            "RAPIDA_ENVIRONMENT"
        )
        self.rapida_region = region or os.environ.get("RAPIDA_REGION")
