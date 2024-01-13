from typing import Optional, Union


class RapidaClientOptions:
    """
    RapidaAI client options
    """

    api_key: str
    region: Union['ap', 'us', 'eu', 'any']
    environment: Optional[str]

    def __init__(self, api_key: str,
                 region: Union['ap', 'us', 'eu', 'any'] = "any",
                 environment: Optional[str] = None) -> None:
        self.api_key = api_key
        self.environment = environment
        self.region = region
