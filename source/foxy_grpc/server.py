import logging

import foxy_grpc.pb2.strings_pb2
import foxy_grpc.pb2.strings_pb2_grpc


class Server(foxy_grpc.pb2.strings_pb2_grpc.StringServiceServicer):
    def GetStrings(self, request, context):
        logging.info(f"GetStrings called: {request}")
        logging.info(f"GetStrings count: {request.count}")
        yield foxy_grpc.pb2.strings_pb2.StringResponse(content="hi")
