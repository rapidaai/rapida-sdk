from typing import Any, Dict, Union, Optional

from rapida.artifacts.protos.endpoint_service.invoker_api_pb2 import InvokerError
from rapida.client.rapida_bridge import RapidaBridge
from rapida.rapida_client_options import RapidaClientOptions
from rapida.exceptions import RapidaException
from rapida.exceptions.exceptions import handle_request_exception
from rapida.exceptions.exceptions import RapidaConfigurationException
import warnings


class RapidaClient:
    # an client/bridge of rapida endpoint
    rapida_bridge: RapidaBridge

    # optional options that can override the configuration for current request
    options: RapidaClientOptions

    def __init__(self, options: Optional[RapidaClientOptions]):
        """

        Args:
            options:
        """

        if options is None:
            options = RapidaClientOptions()

        if options.rapida_api_key is None or len(options.rapida_api_key) == 0:
            raise RapidaConfigurationException("The provided API key is invalid.")

        if options.rapida_endpoint_url is None or len(options.rapida_endpoint_url) == 0:
            raise RapidaConfigurationException("The provided endpoint URL is invalid.")

        self.options = options
        self.rapida_bridge = RapidaBridge(
            service_url=options.rapida_endpoint_url,
            rapida_api_key=options.rapida_api_key,
            rapida_region=options.rapida_region.get(),
            rapida_environment=options.rapida_environment.get(),
        )

    def __validate_endpoint_params(
            self,
            rapida_endpoint: int,
            rapida_endpoint_version: str,
    ) -> None:
        if rapida_endpoint is None:
            raise Exception(
                "The endpoint key is required. Please provide a endpoint key.",
            )

        if rapida_endpoint_version is None:
            warnings.warn(
                "The version is required. Default latest will be used.",
            )

    async def invoke(
            self,
            endpoint: int,
            endpoint_version: str,
            inputs: Dict[str, str],
            metadata: Dict[str, str],
            options: Dict[str, Any],
    ):
        """
        Invokes a deployment with the specified key.

        Args:
            inputs: Dictionary of input parameters for the prompts
            metadata: Dictionary of metadata for the current execution
            options: Dictionary of options for the override parameters for the model
            endpoint (int): The endpoint key.
            endpoint_version (str): The endpoint version.
        Returns:
            `Deployment`: The invoked deployment.

        Raises:
            `RequestException`: If the invocation request fails.
        """
        self.__validate_endpoint_params(
            rapida_endpoint=endpoint,
            rapida_endpoint_version=endpoint_version,
        )

        response = await self.rapida_bridge.make_invoke_call(
            endpoint,
            endpoint_version,
            inputs,
            metadata,
            options,
        )

        if response.success:
            return response

        self.handle_deployment_exception(response.error)

    async def update_metadata(self, rapida_audit_id: int, rapida_metadata: Dict):
        """
        Invokes a audit update with the specified key.

        Args:
            rapida_audit_id (int): The rapida_audit_id key.
            rapida_metadata (dict, optional): Additional metadata to include with the invocation. Defaults to None.

        Returns:
            `Deployment`: The invoked deployment.

        Raises:
            `RequestException`: If the invocation request fails.
        """

        response = await self.rapida_bridge.make_update_call(
            rapida_audit_id, rapida_metadata
        )

        if response.success:
            return response

        self.handle_deployment_exception(response.error)

    async def probe(self, rapida_audit_id: int):
        response = await self.rapida_bridge.make_probe_call(rapida_audit_id)

        if response.success:
            return response

        self.handle_deployment_exception(response.error)

    def handle_deployment_exception(self, error: Union[None, InvokerError]):
        """
        Handling exception for all the common endpoint error
        Args:
            error: An instance of invokeError if found in response

        """
        if error is not None:
            handle_request_exception(error)

        raise RapidaException(
            code=500,
            message="An unknown error occurred.",
            source="internal client error",
        )
