import warnings
from typing import Dict, Union, Optional, Tuple, Mapping
from rapida.artifacts.protos.invoker_api_pb2 import InvokerError
from rapida.client.rapida_bridge import RapidaBridge
from rapida.client.response_wrapper import InvokeResponseWrapper
from rapida.rapida_client_options import RapidaClientOptions
from rapida.exceptions import RapidaException
from rapida.exceptions.exceptions import handle_request_exception
from rapida.exceptions.exceptions import RapidaConfigurationException
from google.protobuf.any_pb2 import Any


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

        self.options = options
        self.rapida_bridge = RapidaBridge(
            service_url=options.rapida_endpoint_url,
            rapida_api_key=options.rapida_api_key,
            rapida_region=options.rapida_region.get(),
            rapida_environment=options.rapida_environment.get(),
            rapida_is_secure=options.is_secure,
        )

    def _endpoint_params(
            self,
            endpoint: Tuple[int, Union[str, None]],
    ) -> Tuple[int, str]:
        rapida_endpoint, rapida_endpoint_version = endpoint
        if rapida_endpoint is None:
            raise Exception(
                "The endpoint key is required. Please provide a endpoint key.",
            )

        if rapida_endpoint_version is None:
            warnings.warn(
                "The version is required. Default latest will be used.",
            )
            return rapida_endpoint, "latest"
        return rapida_endpoint, rapida_endpoint_version

    def _options(self, options: Optional[Dict[str, Any]]) -> Dict[str, str]:

        """

        Args:
            options:

        Returns:

        """
        allowed_options = ["cache", "retry_count"]
        _extras: Dict[str, str] = {}

        if options is None:
            return _extras

        for key, value in options.items():
            if key in allowed_options:
                _extras[key] = str(value)
        return _extras

    async def invoke(
            self,
            endpoint: Tuple[int, Union[str, None]],
            inputs: Mapping[str, Any],
            metadata: Optional[Dict[str, str]] = None,
            options: Optional[Dict[str, Any]] = None,
    ) -> InvokeResponseWrapper:
        """
        Invokes a deployment with the specified key.

        Args:
            inputs: Dictionary of input parameters for the prompts
            metadata: Dictionary of metadata for the current execution
            options: Dictionary of options for the override parameters for the model
            endpoint (int, str): The endpoint key.
        Returns:
            `Deployment`: The invoked deployment.

        Raises:
            `RequestException`: If the invocation request fails.
        """
        endpoint_id, endpoint_version = self._endpoint_params(endpoint)
        options: Dict[str, str] = self._options(options)
        response = await self.rapida_bridge.make_invoke_call(
            endpoint_id,
            endpoint_version,
            inputs,
            metadata,
            options,
        )

        if response.is_success():
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
