# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import protocol_pb2 as protocol__pb2

GRPC_GENERATED_VERSION = '1.70.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in protocol_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class StringServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetStrings = channel.unary_stream(
                '/foxy_grpc.protocol.StringService/GetStrings',
                request_serializer=protocol__pb2.StringRequest.SerializeToString,
                response_deserializer=protocol__pb2.StringResponse.FromString,
                _registered_method=True)


class StringServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetStrings(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StringServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetStrings': grpc.unary_stream_rpc_method_handler(
                    servicer.GetStrings,
                    request_deserializer=protocol__pb2.StringRequest.FromString,
                    response_serializer=protocol__pb2.StringResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'foxy_grpc.protocol.StringService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('foxy_grpc.protocol.StringService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class StringService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetStrings(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/foxy_grpc.protocol.StringService/GetStrings',
            protocol__pb2.StringRequest.SerializeToString,
            protocol__pb2.StringResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
