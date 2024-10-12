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


import logging
from typing import AsyncIterator, Dict, List, Optional, Mapping
from google.protobuf.json_format import ParseDict
from google.protobuf.any_pb2 import Any
from google.protobuf.struct_pb2 import Struct
from rapida.client.response_wrapper import InvokeResponseWrapper
from rapida.artifacts.protos import (
    common_pb2,
    integration_api_pb2,
    integration_api_pb2_grpc,
    invoker_api_pb2,
    invoker_api_pb2_grpc,
)
from rapida.client.grpc_bridge import GRPCBridge

_log = logging.getLogger("rapida.client.rapida_bridge")


class RapidaBridge(GRPCBridge):
    def __init__(
        self,
        service_url: str,
        rapida_api_key: str,
        rapida_region: str,
        rapida_environment: str,
        rapida_source: str,
        rapida_is_secure: bool,
    ):
        """

        Args:
            service_url:
            rapida_api_key:
            rapida_region:
            rapida_environment:
        """
        super().__init__(
            service_url,
            rapida_api_key,
            rapida_region,
            rapida_environment,
            rapida_source,
            rapida_is_secure,
        )

    async def make_invoke_call(
        self,
        endpoint_id: int,
        version: str,
        body_params: Mapping[str, Any],
        metadata: Optional[Dict[str, str]],
        override_options: Optional[Dict[str, str]],
    ) -> InvokeResponseWrapper:
        """
        Endpoint request to the rapida api endpoint servers
        Args:
            endpoint_id:
            version:
            body_params:
            metadata:
            override_options:

        Returns:

        """
        response = await self.fetch(
            stub=invoker_api_pb2_grpc.DeploymentStub,
            attr="Invoke",
            message_type=invoker_api_pb2.InvokeRequest(
                endpoint=invoker_api_pb2.EndpointDefinition(
                    endpointId=endpoint_id, version=version
                ),
                args=body_params,
                metadata=metadata,
                options=override_options,
            ),
            preserving_proto_field_name=True,
        )

        return InvokeResponseWrapper(
            ParseDict(response, invoker_api_pb2.InvokeResponse())
        )

    async def make_probe_call(
        self, rapida_audit_id: int
    ) -> invoker_api_pb2.ProbeResponse:
        """
        To get details about the request for given request id
        Args:
            rapida_audit_id: an audit id represent the request

        Returns:

        """
        response = await self.fetch(
            stub=invoker_api_pb2_grpc.DeploymentStub,
            attr="Probe",
            message_type=invoker_api_pb2.ProbeRequest(requestId=rapida_audit_id),
            preserving_proto_field_name=True,
        )
        return ParseDict(
            response, invoker_api_pb2.ProbeResponse(), ignore_unknown_fields=True
        )

    async def make_update_call(
        self, rapida_audit_id: int, rapida_metadata: Optional[Dict[str, str]]
    ) -> invoker_api_pb2.UpdateResponse:
        """
        Provide an interface to update the metadata for executed request
        Args:
            rapida_audit_id: an audit id represent the request
            rapida_metadata: data that will be extended current metadata list

        Returns:

        """
        response = await self.fetch(
            stub=invoker_api_pb2_grpc.DeploymentStub,
            attr="Update",
            message_type=invoker_api_pb2.UpdateRequest(
                requestId=rapida_audit_id,
                metadata=rapida_metadata,
            ),
            preserving_proto_field_name=True,
            # including_default_value_fields=True,
        )

        return ParseDict(
            response, invoker_api_pb2.UpdateResponse(), ignore_unknown_fields=True
        )

    async def chat(
        self,
        cred: Dict,
        provider: str,
        model: str,
        conversations: List[common_pb2.Message],
        tool_definitions: List[integration_api_pb2.ToolDefinition],
        model_parameters: List[integration_api_pb2.ModelParameter],
        meta: Mapping[str, str] = None,
    ) -> integration_api_pb2.ChatResponse:
        """
        Asynchronously initiates a chat interaction with the Rapida service.

        This method sends a chat request to the Rapida service and processes the response.
        It utilizes gRPC to communicate with the service, specifically calling the
        'UpdateMetadata' method of the RapidaServiceStub.

        The function performs the following steps:
        1. Sends a chat request to the Rapida service using the 'fetch' method.
        2. Waits for the asynchronous response from the service.
        3. Parses the received response into a ChatResponse object.

        Returns:
            integration_api_pb2.ChatResponse: The processed response from the Rapida service,
            containing the chat interaction results.

        Note:
            - This method uses the 'fetch' utility to handle the gRPC communication.
            - The 'preserving_proto_field_name' parameter is set to True to maintain
            the original field names in the protocol buffer message.
            - The response is parsed using the 'ParseDict' function, which converts
            the dictionary response into a ChatResponse protocol buffer object.
            - Unknown fields in the response are ignored during parsing.

        Raises:
            Any exceptions that might occur during the gRPC communication or response parsing.

        Example usage:
            chat_response = await rapida_bridge_instance.chat()
            # Process the chat_response as needed
        """

        credentials = Struct()
        for k, v in cred.items():
            credentials.update({k: v})

        response = await self.fetch(
            stub=integration_api_pb2_grpc.RapidaServiceStub,
            attr="Chat",
            message_type=integration_api_pb2.ChatRequest(
                credential=integration_api_pb2.Credential(value=credentials),
                model=f"{provider}/{model}",
                conversations=conversations,
                toolDefinitions=tool_definitions,
                modelParameters=model_parameters,
                additionalData=meta,
            ),
            preserving_proto_field_name=True,
        )

        return ParseDict(
            response, integration_api_pb2.ChatResponse(), ignore_unknown_fields=True
        )

    async def generate(
        self,
        cred: Dict,
        provider: str,
        model: str,
        system_prompt: str,
        prompt: str,
        model_parameters: Mapping[str, str] = None,
        meta: Mapping[str, str] = None,
    ) -> integration_api_pb2.GenerateResponse:
        """
        Prepares and sends a generation request to the Rapida service.

        This function:
        1. Converts credentials and model parameters to the required format
        2. Constructs a GenerateRequest message with the provided inputs
        3. Sends the request to the Rapida service using gRPC
        4. Parses and returns the response as a GenerateResponse object

        Args:
            cred (dict): Credentials for authentication
            system_prompt (str): System prompt for the generation
            prompt (str): User prompt for the generation
            provider (str): The AI provider to use
            model (str): The specific model to use
            model_parameters (dict): Additional parameters for the model
            meta (dict): Any additional metadata

        Returns:
            integration_api_pb2.GenerateResponse: The parsed response from the service
        """
        credentials = Struct()
        for k, v in cred.items():
            credentials.update({k: v})

        args: List[integration_api_pb2.ModelParameter] = []
        for k, v in model_parameters.items():
            args.append(
                integration_api_pb2.ModelParameter(
                    key=k,
                    value=v,
                )
            )

        response = await self.fetch(
            stub=integration_api_pb2_grpc.RapidaServiceStub,
            attr="Generate",
            message_type=integration_api_pb2.GenerateRequest(
                credential=credentials,
                systemPrompt=system_prompt,
                prompt=prompt,
                model=f"{provider}/{model}",
                modelParameters=args,
                additionalData=meta,
            ),
            preserving_proto_field_name=True,
        )

        return ParseDict(
            response, integration_api_pb2.GenerateResponse(), ignore_unknown_fields=True
        )

    async def embedding(
        self,
        cred: Dict,
        provider: str,
        model: str,
        contents: List[str],
        model_parameters: Mapping[str, str] = None,
        meta: Mapping[str, str] = None,
    ) -> integration_api_pb2.EmbeddingResponse:

        credentials = Struct()
        for k, v in cred.items():
            credentials.update({k: v})

        args: List[integration_api_pb2.ModelParameter] = []
        for k, v in model_parameters.items():
            args.append(
                integration_api_pb2.ModelParameter(
                    key=k,
                    value=v,
                )
            )

        _content: Mapping[int, str] = {}
        for i, val in enumerate(contents):
            _content[i] = val

        response = await self.fetch(
            stub=integration_api_pb2_grpc.RapidaServiceStub,
            attr="Embedding",
            message_type=integration_api_pb2.EmbeddingRequest(
                credential=credentials,
                model=f"{provider}/{model}",
                modelParameters=args,
                additionalData=meta,
                content=_content,
            ),
            preserving_proto_field_name=True,
        )

        return ParseDict(
            response,
            integration_api_pb2.EmbeddingResponse(),
            ignore_unknown_fields=True,
        )

    async def chat_stream(
        self,
        cred: Dict,
        provider: str,
        model: str,
        conversations: List[common_pb2.Message],
        tool_definitions: List[integration_api_pb2.ToolDefinition],
        model_parameters: List[integration_api_pb2.ModelParameter],
        meta: Mapping[str, str] = None,
    ) -> AsyncIterator[integration_api_pb2.ChatResponse]:
        """
        Asynchronously initiates a chat interaction with the Rapida service and streams the responses.

        This method sends a chat request to the Rapida service and handles streaming responses.
        It utilizes gRPC to communicate with the service, specifically calling the
        'StreamChat' method of the RapidaServiceStub.

        The function performs the following steps:
        1. Sends a chat request to the Rapida service using the 'fetch_stream_response' method.
        2. Asynchronously iterates over the streaming responses from the service.
        3. Parses each received response into a ChatResponse object.

        Returns:
            AsyncIterator[integration_api_pb2.ChatResponse]: The streamed responses from the Rapida service,
            containing the chat interaction results.

        Note:
            - This method uses the 'fetch_stream' utility to handle the gRPC communication.
            - The 'preserving_proto_field_name' parameter is set to True to maintain
            the original field names in the protocol buffer message.
            - Each response is parsed using the 'ParseDict' function, which converts
            the dictionary response into a ChatResponse protocol buffer object.
            - Unknown fields in the response are ignored during parsing.

        Raises:
            Any exceptions that might occur during the gRPC communication or response parsing.

        Example usage:
            async for chat_response in rapida_bridge_instance.chat_stream():
                # Process each chat_response as needed
        """

        credentials = Struct()
        for k, v in cred.items():
            credentials.update({k: v})

        # Stream the chat response from the gRPC server
        async for response in self.fetch_stream(
            stub=integration_api_pb2_grpc.RapidaServiceStub,
            attr="StreamChat",
            message_type=integration_api_pb2.ChatRequest(
                credential=integration_api_pb2.Credential(value=credentials),
                model=f"{provider}/{model}",
                conversations=conversations,
                toolDefinitions=tool_definitions,
                modelParameters=model_parameters,
                additionalData=meta,
            ),
            preserving_proto_field_name=True,
        ):
            yield ParseDict(
                response, integration_api_pb2.ChatResponse(), ignore_unknown_fields=True
            )
