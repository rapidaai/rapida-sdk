"""
author: prashant.srivastav
"""

# from typing import Union

from google.protobuf.struct_pb2 import Struct
from google.protobuf.json_format import ParseDict
from rapida.artifacts.protos.endpoint_service import (
    invoker_api_pb2,
    invoker_api_pb2_grpc
)
from rapida.client.grpc_client import GRPCBridge
from rapida.exceptions.exceptions import RapidaException


class RapidaBridge(GRPCBridge):

    @classmethod
    def __init__(cls, service_url: str):
        super().__init__(service_url)

    @classmethod
    async def make_call(cls, method_name: str, endpointId: int, version: str, body_params: dict, options: dict[str, str]):
        """
        :param method_name: ["Invoke", "Probe"]
        """
        if method_name not in ["Invoke", "Probe"]:
            raise RapidaException(
                    code=500,
                    message="Unimplemented method",
                    source="",
                )

        a:Struct = Struct()
        a.update(body_params)

        response = await cls.fetch(
            stub= invoker_api_pb2_grpc.DeploymentStub,
            attr= method_name,
            message_type= invoker_api_pb2.InvokeRequest(
                endpoint= invoker_api_pb2.EndpointDefnition(
                    endpointId= endpointId,
                    version= version
                ),
                args= a,
                options= options,
            ),
            preserving_proto_field_name=True,
            # including_default_value_fields=True,
        )

        message = ParseDict(response, invoker_api_pb2.InvokeResponse())
        print(message)

