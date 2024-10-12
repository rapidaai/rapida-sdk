#  Copyright (c) 2024. Rapida
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#  THE SOFTWARE.
#
#  Author: Prashant <prashant@rapida.ai>

import warnings
from typing import AsyncIterator, Dict, List, Union, Optional, Tuple, Mapping
from rapida.client.rapida_bridge import RapidaBridge
from rapida.client.response_wrapper import (
    ToolDefinition,
    InvokeResponseWrapper,
    Message,
    ToolDefinition,
)
from rapida.rapida_client_options import RapidaClientOptions
from rapida.exceptions import RapidaException
from rapida.exceptions.exceptions import handle_request_exception
from rapida.exceptions.exceptions import RapidaConfigurationException
from rapida.artifacts.protos import common_pb2, integration_api_pb2
from rapida.artifacts.protos.invoker_api_pb2 import InvokerError
from google.protobuf.any_pb2 import Any


class RapidaClient:
    # an client/bridge of rapida endpoint
    rapida_bridge: RapidaBridge

    # optional options that can override the configuration for current request
    options: RapidaClientOptions


class RapidaEndpointClient(RapidaClient):

    def __init__(self, options: Optional[RapidaClientOptions]):
        """
        This is the constructor for the RapidaEndpointClient class.

        It initializes the client with the provided options or creates default options if none are given.
        The constructor performs the following tasks:

        1. Checks if options are provided, and if not, creates a default RapidaClientOptions object.
        2. Validates the API key, raising a RapidaConfigurationException if it's invalid or missing.
        3. Stores the options for future use.
        4. Creates a RapidaBridge instance with the following parameters:
           - service_url: The endpoint URL for the Rapida service
           - rapida_api_key: The API key for authentication
           - rapida_region: The region setting for the Rapida service
           - rapida_environment: The environment setting (e.g., production, staging)
           - rapida_is_secure: A boolean indicating whether to use secure connections

        This initialization sets up the client for making API calls to the Rapida service
        with the specified configuration options.
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
            rapida_source=options.rapida_source.get(),
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
        """
        Probe request for given endpoint audit id
        Args:
            audit_id: request id for probe

        """
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


class RapidaGatewayClient(RapidaClient):
    def __init__(self, options: Optional[RapidaClientOptions]):
        if options is None:
            options = RapidaClientOptions()

        if options.rapida_api_key is None or len(options.rapida_api_key) == 0:
            raise RapidaConfigurationException("The provided API key is invalid.")

        self.options = options
        self.rapida_bridge = RapidaBridge(
            service_url=options.rapida_gateway_url,
            rapida_api_key=options.rapida_api_key,
            rapida_region=options.rapida_region.get(),
            rapida_source=options.rapida_source.get(),
            rapida_environment=options.rapida_environment.get(),
            rapida_is_secure=options.is_secure,
        )

    async def chat(
        self,
        credentials: Dict,
        provider: str,
        model: str,
        conversations: List[Message],
        tools: List[ToolDefinition] = None,
        model_parameters: Mapping[str, Any] = None,
        meta: Mapping[str, str] = None,
    ) -> integration_api_pb2.ChatResponse:

        conv: List[common_pb2.Message] = []
        for i, msg in enumerate(conversations):
            conv.append(msg.to_message())

        args: List[integration_api_pb2.ModelParameter] = []
        if model_parameters is not None:
            for k, v in model_parameters.items():
                args.append(
                    integration_api_pb2.ModelParameter(
                        key=k,
                        value=v,
                    )
                )

        tool_definitions: List[integration_api_pb2.ToolDefinition] = []
        for v in tools:
            tool_definitions.append(v.to_tool_definition())

        return await self.rapida_bridge.chat(
            cred=credentials,
            provider=provider,
            model=model,
            conversations=conv,
            tool_definitions=tool_definitions,
            model_parameters=args,
            meta=meta,
        )

    async def chat_stream(
        self,
        credentials: Dict,
        provider: str,
        model: str,
        conversations: List[Message],
        tools: List[ToolDefinition] = None,
        model_parameters: Mapping[str, Any] = None,
        meta: Mapping[str, str] = None,
    ) -> AsyncIterator[integration_api_pb2.ChatResponse]:

        conv: List[common_pb2.Message] = []
        for i, msg in enumerate(conversations):
            conv.append(msg.to_message())

        args: List[integration_api_pb2.ModelParameter] = []
        if model_parameters is not None:
            for k, v in model_parameters.items():
                args.append(
                    integration_api_pb2.ModelParameter(
                        key=k,
                        value=v,
                    )
                )

        tool_definitions: List[integration_api_pb2.ToolDefinition] = []
        for v in tools:
            tool_definitions.append(v.to_tool_definition())

        async for response in self.rapida_bridge.chat_stream(
            cred=credentials,
            provider=provider,
            model=model,
            conversations=conv,
            tool_definitions=tool_definitions,
            model_parameters=args,
            meta=meta,
        ):
            yield response

    async def generate(
        self,
        cred: Dict,
        provider: str,
        model: str,
        system_prompt: str,
        prompt: str,
        model_parameters: Mapping[str, str],
        meta: Mapping[str, str],
    ):

        return await self.rapida_bridge.generate(
            cred=cred,
            provider=provider,
            model=model,
            system_prompt=system_prompt,
            prompt=prompt,
            model_parameters=model_parameters,
            meta=meta,
        )

    async def embedding(
        self,
        cred: Dict,
        provider: str,
        model: str,
        contents: List[str],
        model_parameters: Mapping[str, str],
        meta: Mapping[str, str],
    ):
        return await self.rapida_bridge.embedding(
            cred=cred,
            provider=provider,
            model=model,
            contents=contents,
            model_parameters=model_parameters,
            meta=meta,
        )


class RapidaAssistantClient(RapidaClient):
    def __init__(self, options: Optional[RapidaClientOptions]):
        if options is None:
            options = RapidaClientOptions()

        if options.rapida_api_key is None or len(options.rapida_api_key) == 0:
            raise RapidaConfigurationException("The provided API key is invalid.")

        self.options = options
        self.rapida_bridge = RapidaBridge(
            service_url=options.rapida_assistant_url,
            rapida_api_key=options.rapida_api_key,
            rapida_region=options.rapida_region.get(),
            rapida_environment=options.rapida_environment.get(),
            rapida_is_secure=options.is_secure,
        )
