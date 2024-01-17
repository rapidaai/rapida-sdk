"""
author: prashant.srivastav
"""
import logging
from typing import Dict, Optional

from google.protobuf.json_format import ParseDict
from google.protobuf.struct_pb2 import Struct

from rapida.artifacts.protos.endpoint_service import (
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
    ):
        """

        Args:
            service_url:
            rapida_api_key:
            rapida_region:
            rapida_environment:
        """
        super().__init__(service_url, rapida_api_key, rapida_region, rapida_environment)

    async def make_invoke_call(
        self,
        endpoint_id: int,
        version: str,
        body_params: Dict,
        metadata: Optional[Dict],
        override_options: Optional[Dict],
    ) -> invoker_api_pb2.InvokeResponse:
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
        _args: Struct = Struct()
        _args.update(body_params)

        _metadata: Struct = Struct()
        if metadata:
            _metadata.update(metadata)

        _override_options: Struct = Struct()
        if _override_options:
            _override_options.update(override_options)

        response = await self.fetch(
            stub=invoker_api_pb2_grpc.DeploymentStub,
            attr="Invoke",
            message_type=invoker_api_pb2.InvokeRequest(
                endpoint=invoker_api_pb2.EndpointDefinition(
                    endpointId=endpoint_id, version=version
                ),
                args=_args,
                metadata=_metadata,
                options=_override_options,
            ),
            preserving_proto_field_name=True,
            # including_default_value_fields=True,
        )

        return ParseDict(response, invoker_api_pb2.InvokeResponse())

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
        self, rapida_audit_id: int, rapida_metadata: Dict
    ) -> invoker_api_pb2.UpdateResponse:
        """
        Provide an interface to update the metadata for executed request
        Args:
            rapida_audit_id: an audit id represent the request
            rapida_metadata: data that will be extended current metadata list

        Returns:

        """
        _metadata: Struct = Struct()
        _metadata.update(rapida_metadata)

        response = await self.fetch(
            stub=invoker_api_pb2_grpc.DeploymentStub,
            attr="UpdateMetadata",
            message_type=invoker_api_pb2.UpdateRequest(
                requestId=rapida_audit_id,
                metadata=_metadata,
            ),
            preserving_proto_field_name=True,
            # including_default_value_fields=True,
        )

        return ParseDict(
            response, invoker_api_pb2.UpdateResponse(), ignore_unknown_fields=True
        )
