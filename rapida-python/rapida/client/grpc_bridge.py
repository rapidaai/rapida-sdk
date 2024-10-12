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
# Base Bridge class for all RPC and gRPC clients.
# - Changing this class will impact all RPC and gRPC clients and consumer service which implement and inherit
#     this class.
# - Considered as core computability layer for all RPC and gRPC clients the CHANGE REQUEST is not allowed.
# - Mostly response being handled with JSON format.
#
#
#  Author: Prashant <prashant@rapida.ai>


import logging
import time
from abc import ABC
from typing import Any, AsyncIterator, Dict

import grpc
from google.protobuf.json_format import MessageToDict
from grpc import UnaryStreamMultiCallable, aio as grpc_aio
from google.protobuf.message import Message
from grpc.aio import Metadata
from grpc.aio._channel import UnaryUnaryMultiCallable

from rapida.constants import (
    HEADER_API_KEY,
    HEADER_ENVIRONMENT_KEY,
    HEADER_REGION_KEY,
    HEADER_SOURCE_KEY,
)
from rapida.exceptions.exceptions import RapidaException

_log = logging.getLogger("rapida.client.grpc_bridge")


class GRPCBridge(ABC):
    """
    Base class for all GRPC bridges.
    """

    # base url as hosts
    service_url: str
    rapida_api_key: str
    rapida_region: str
    rapida_environment: str
    rapida_source: str
    rapida_is_secure: bool

    @classmethod
    def __init__(
        cls,
        service_url: str,
        rapida_api_key: str,
        rapida_region: str,
        rapida_environment: str,
        rapida_source: str,
        rapida_is_secure: bool,
    ):
        """
        Args:
            service_url: a url where the endpoint service is deployed
            rapida_api_key: a api keys to authenticate and authorize the request made to rapida servers (Please find the docs <a>docs.rapida.ai</a>
            rapida_region: specify the region to accelerate the request if it's specific as per client need
            rapida_source: source of the request for rapida request later it will become important for routing and parsing the information
            rapida_environment: a tag to represent the env currently (production and development is supported)
        """
        cls.service_url = service_url
        cls.rapida_api_key = rapida_api_key
        cls.rapida_region = rapida_region
        cls.rapida_source = rapida_source
        cls.rapida_environment = rapida_environment
        cls.rapida_is_secure = rapida_is_secure

    @classmethod
    def channel(cls):
        if not cls.rapida_is_secure:
            return grpc_aio.insecure_channel(cls.service_url)
        return grpc_aio.secure_channel(cls.service_url, grpc.ssl_channel_credentials())
        # as channel:

    @classmethod
    async def fetch(
        cls,
        stub: Any,
        attr: str,
        message_type: Message,
        **unmarshal_options,
    ) -> Dict[str, Any]:
        """
        Generic requestor
        :param stub:
        :param attr:
        :param message_type:
        :param unmarshal_options
        Args:
            including_default_value_fields: If True, singular primitive fields,
                repeated fields, and map fields will always be serialized.  If
                False, only serialize non-empty fields.  Singular message fields
                and one of fields are not affected by this option.
            preserving_proto_field_name: If True, use the original proto field
                names as defined in the .proto file. If False, convert the field
                names to lowerCamelCase.
            use_integers_for_enums: If true, print integers instead of enum names.
            descriptor_pool: A Descriptor Pool for resolving types. If None uses the
                default.
            float_precision: If set, use this to specify float field valid digits.
        :return:
        """
        started_request = time.time()
        try:
            _log.debug(f"grpc_bridge: in span of {attr}")
            async with cls.channel() as channel:
                _log.debug(f"grpc_bridge: created secure channel for {cls.service_url}")

                # get attribute from stub
                unary_unary: UnaryUnaryMultiCallable = getattr(stub(channel), attr)
                # metadata for request
                _metadata: Metadata = Metadata()

                _metadata.add(HEADER_API_KEY, cls.rapida_api_key)
                _metadata.add(HEADER_ENVIRONMENT_KEY, cls.rapida_environment)
                _metadata.add(HEADER_REGION_KEY, cls.rapida_region)
                _metadata.add(HEADER_SOURCE_KEY, cls.rapida_source)

                # request executed with asynchronous invocation of a unary-call RPC.
                results = await unary_unary(request=message_type, metadata=_metadata)
                # parsing result and unmarshalling the result with given options
                json_result = MessageToDict(results, **unmarshal_options)
                _log.info(
                    f"{cls.__qualname__} {attr} [status:OK request:{time.time() - started_request}s]"
                )
                return json_result
        except grpc_aio.AioRpcError as ex:
            # if there is error from inter service client communication then log and throw scoped exception
            _log.error(
                f"{cls.__qualname__} {attr} [status:NOT_OK request:{time.time() - started_request}s]"
            )
            raise RapidaException(message=str(ex), code=500, source=__name__)

    @classmethod
    async def fetch_stream(
        cls,
        stub: Any,
        attr: str,
        message_type: Message,  # Unary request
        **unmarshal_options,
    ) -> AsyncIterator[Dict[str, Any]]:
        """
        Generic requestor for unary request with streaming response
        :param stub:
        :param attr:
        :param message_type: Unary request message
        :param unmarshal_options: Options to control unmarshalling of the protobuf result.
        """
        started_request = time.time()
        try:
            _log.debug(f"grpc_bridge: in span of {attr}")
            async with cls.channel() as channel:
                _log.debug(f"grpc_bridge: created secure channel for {cls.service_url}")

                # Get unary-stream method from the stub (request once, receive a stream)
                unary_stream: UnaryStreamMultiCallable = getattr(stub(channel), attr)

                # Metadata for the request
                _metadata: Metadata = Metadata()
                _metadata.add(HEADER_API_KEY, cls.rapida_api_key)
                _metadata.add(HEADER_ENVIRONMENT_KEY, cls.rapida_environment)
                _metadata.add(HEADER_REGION_KEY, cls.rapida_region)
                _metadata.add(HEADER_SOURCE_KEY, cls.rapida_source)

                # Send the unary request and receive a stream of responses
                async for response in unary_stream(
                    request=message_type, metadata=_metadata
                ):
                    # Unmarshal each result with the given options
                    json_result = MessageToDict(response, **unmarshal_options)
                    _log.info(
                        f"{cls.__qualname__} {attr} [status:OK request:{time.time() - started_request}s]"
                    )
                    # Yield each response as part of the stream
                    yield json_result
        except grpc_aio.AioRpcError as ex:
            # Handle errors from inter-service client communication
            _log.error(
                f"{cls.__qualname__} {attr} [status:NOT_OK request:{time.time() - started_request}s]"
            )
            raise RapidaException(message=str(ex), code=500, source=__name__)
