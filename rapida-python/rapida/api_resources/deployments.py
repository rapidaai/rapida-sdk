from typing import Any, Dict

from rapida.client.rapida_bridge import RapidaBridge
from rapida.client_options import RapidaClientOptions
from rapida.exceptions.exceptions import handle_request_exception


class RapidaData:

    def __init__(self, options: RapidaClientOptions, rapida_bridge: RapidaBridge):
        self.options = options
        self.rapida_bridge = rapida_bridge

    def __validate_endpoint_params(
            self,
            rapida_endpoint: int,
            rapida_endpoint_version: str,
            rapida_environment: str,
    ) -> None:
        if rapida_endpoint is None:
            raise Exception(
                "The endpoint key is required. Please provide a endpoint key.",
            )

        if rapida_endpoint_version is None:
            raise Warning(
                "The version is required. Default latest will be used.",
            )

        if rapida_environment is None:
            raise Warning(
                "The environment is required. Default Test will be used.",
            )

    async def invoke(
            self,
            rapida_endpoint: int,
            rapida_endpoint_version: str,
            rapida_environment: str,
            rapida_inputs: Dict[str, str],
            rapida_metadata: Dict[str, str],
            rapida_options: Dict[str, Any]
    ):
        """
        Invokes a deployment with the specified key.

        Args:
            rapida_environment: Environment to run
            rapida_inputs: Dictionary of input parameters for the prompts
            rapida_metadata: Dictionary of metadata for the current execution
            rapida_options: Dictionary of options for the overide parameters for the model
            rapida_endpoint (int): The endpoint key.
            rapida_endpoint_version (str): The endpoint version.
        Returns:
            `Deployment`: The invoked deployment.

        Raises:
            `RequestException`: If the invocation request fails.
        """
        self.__validate_endpoint_params(rapida_endpoint=rapida_endpoint,
                                        rapida_endpoint_version=rapida_endpoint_version,
                                        rapida_environment=rapida_environment)

        response = await self.rapida_bridge.make_invoke_call(rapida_endpoint, rapida_endpoint_version,
                                                rapida_inputs, rapida_metadata,
                                                rapida_options)

        if response.ok is None or response.status_code != 200:
            handle_request_exception(response)

        return response

    async def update_metadata(self, rapida_audit_id: int, rapida_metadata: dict):
        """
        Invokes a audit update with the specified key.

        Args:
            rapida_audit_id (int): The rapida_audit_id key.
            metadata (dict, optional): Additional metadata to include with the invocation. Defaults to None.

        Returns:
            `Deployment`: The invoked deployment.

        Raises:
            `RequestException`: If the invocation request fails.
        """

        response = await self.rapida_bridge.make_update_call(rapida_audit_id, rapida_metadata)

        if response.ok is None or response.status_code != 200:
            handle_request_exception(response)

        return response

    async def probe(self, rapida_audit_id: str):
        response = await self.rapida_bridge.make_probe_call(rapida_audit_id)

        if response.ok is None or response.status_code != 200:
            handle_request_exception(response)

        return response
