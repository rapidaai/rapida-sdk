"""
author: prashant.srivastav
"""
import logging
from typing import Dict, Optional, Mapping
from google.protobuf.json_format import ParseDict
from google.protobuf.any_pb2 import Any


from rapida.client.response_wrapper import InvokeResponseWrapper
from rapida.artifacts.protos import (
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
            # including_default_value_fields=True,
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
            attr="UpdateMetadata",
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
