"""
author: prashant.srivastav
"""

# from typing import Union

from typing import Any, Dict, List
from google.protobuf.struct_pb2 import Struct
from google.protobuf.any_pb2 import Any as ProtoAny
from google.protobuf.json_format import Parse

import ipdb

from google.protobuf.internal import containers as _containers

from google.protobuf.json_format import ParseDict
from rapida.artifacts.protos.endpoint_service import (
    invoker_api_pb2,
    invoker_api_pb2_grpc
)
from rapida.client.grpc_client import GRPCBridge
from rapida.exceptions.exceptions import RapidaException

class RapidaBridge(GRPCBridge):

    @classmethod
    def __init__(cls, service_url: str, rapida_api_key:str, rapida_region:str, rapida_environment:str):
        super().__init__(service_url, rapida_api_key, rapida_region, rapida_environment)

    # rapida_api_key: str
    # rapida_endpoint_url: str
    # rapida_region: Union['ap', 'us', 'eu', 'any']
    # rapida_environment: Optional[str]

    @classmethod
    async def make_invoke_call(cls, endpoint_id: int, version: str, body_params: Dict, metadata: Dict, options: Dict):
        a:Struct = Struct()
        a.update(body_params)

        b:Struct = Struct()
        b.update(metadata)

        c:Struct = Struct()
        c.update(options)

        response = await cls.fetch(
            stub= invoker_api_pb2_grpc.DeploymentStub,
            attr="Invoke",
            message_type = invoker_api_pb2.InvokeRequest(
                endpoint=invoker_api_pb2.EndpointDefinition(
                    endpointId=endpoint_id,
                    version=version
                ),
                args=a,
                metadata=b,
                options=c,
            ),
            preserving_proto_field_name=True,
            # including_default_value_fields=True,
        )

        return ParseDict(response, invoker_api_pb2.InvokeResponse())

    async def make_probe_call(cls, requestId:int):

        response = await cls.fetch(
            stub= invoker_api_pb2_grpc.DeploymentStub,
            attr="Probe",
            message_type = invoker_api_pb2.ProbeRequest(
                requestId=requestId
            ),
            preserving_proto_field_name=True,
            # including_default_value_fields=True,
        )

        return ParseDict(response, invoker_api_pb2.ProbeResponse())


    async def make_update_call(cls, rapida_audit_id:int, rapida_metadata: Dict):
        a:Struct = Struct()
        a.update(rapida_metadata)

        response = await cls.fetch(
            stub= invoker_api_pb2_grpc.DeploymentStub,
            attr="UpdateMetadata",
            message_type = invoker_api_pb2.UpdateRequest(
                requestId=rapida_audit_id,
                metadata=a,
            ),
            preserving_proto_field_name=True,
            # including_default_value_fields=True,
        )

        return ParseDict(response, invoker_api_pb2.UpdateResponse())