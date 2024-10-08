# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import rapida.artifacts.protos.invoker_api_pb2 as invoker__api__pb2

GRPC_GENERATED_VERSION = '1.65.4'
GRPC_VERSION = grpc.__version__
EXPECTED_ERROR_RELEASE = '1.66.0'
SCHEDULED_RELEASE_DATE = 'August 6, 2024'
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    warnings.warn(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in invoker_api_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
        + f' This warning will become an error in {EXPECTED_ERROR_RELEASE},'
        + f' scheduled for release on {SCHEDULED_RELEASE_DATE}.',
        RuntimeWarning
    )


class DeploymentStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Invoke = channel.unary_unary(
                '/endpoint_api.Deployment/Invoke',
                request_serializer=invoker__api__pb2.InvokeRequest.SerializeToString,
                response_deserializer=invoker__api__pb2.InvokeResponse.FromString,
                _registered_method=True)
        self.Update = channel.unary_unary(
                '/endpoint_api.Deployment/Update',
                request_serializer=invoker__api__pb2.UpdateRequest.SerializeToString,
                response_deserializer=invoker__api__pb2.UpdateResponse.FromString,
                _registered_method=True)
        self.Probe = channel.unary_unary(
                '/endpoint_api.Deployment/Probe',
                request_serializer=invoker__api__pb2.ProbeRequest.SerializeToString,
                response_deserializer=invoker__api__pb2.ProbeResponse.FromString,
                _registered_method=True)


class DeploymentServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Invoke(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Probe(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DeploymentServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Invoke': grpc.unary_unary_rpc_method_handler(
                    servicer.Invoke,
                    request_deserializer=invoker__api__pb2.InvokeRequest.FromString,
                    response_serializer=invoker__api__pb2.InvokeResponse.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=invoker__api__pb2.UpdateRequest.FromString,
                    response_serializer=invoker__api__pb2.UpdateResponse.SerializeToString,
            ),
            'Probe': grpc.unary_unary_rpc_method_handler(
                    servicer.Probe,
                    request_deserializer=invoker__api__pb2.ProbeRequest.FromString,
                    response_serializer=invoker__api__pb2.ProbeResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'endpoint_api.Deployment', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('endpoint_api.Deployment', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Deployment(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Invoke(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/endpoint_api.Deployment/Invoke',
            invoker__api__pb2.InvokeRequest.SerializeToString,
            invoker__api__pb2.InvokeResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/endpoint_api.Deployment/Update',
            invoker__api__pb2.UpdateRequest.SerializeToString,
            invoker__api__pb2.UpdateResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Probe(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/endpoint_api.Deployment/Probe',
            invoker__api__pb2.ProbeRequest.SerializeToString,
            invoker__api__pb2.ProbeResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
