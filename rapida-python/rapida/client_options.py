from typing import Optional, Union


class RapidaClientOptions:
    """
    RapidaAI client options
    """

    rapida_api_key: str
    rapida_endpoint_url: str
    rapida_region: Union['ap', 'us', 'eu', 'any']
    rapida_environment: Optional[str]

    def __init__(self, rapida_api_key: str, rapida_endpoint_url:str,
                 rapida_region: Union['ap', 'us', 'eu', 'any'] = "any",
                 rapida_environment: Optional[str] = None) -> None:
        self.rapida_api_key = rapida_api_key
        self.rapida_endpoint_url = rapida_endpoint_url
        self.rapida_environment = rapida_environment
        self.rapida_region = rapida_region
