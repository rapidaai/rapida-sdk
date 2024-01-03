from typing import Optional


class RapidaClientOptions:
    def __init__(self, api_key: str, environment: Optional[str] = None) -> None:
        self.api_key = api_key
        self.environment = environment
