import logging
import uuid

import foxy_grpc.pb2.strings_pb2
import foxy_grpc.pb2.strings_pb2_grpc

class Server(foxy_grpc.pb2.strings_pb2_grpc.StringServiceServicer):
    def GetStrings(self, request, context):
        logging.info(f"GetStrings called: <{request}>")
        if request.forever:
            i = 0
            while True:
                u = uuid.uuid4()
                yield foxy_grpc.pb2.strings_pb2.StringResponse(content=f"{i}: {u}")
                i += 1
        else:
            for i in range(request.count):
                u = uuid.uuid4()
                yield foxy_grpc.pb2.strings_pb2.StringResponse(content=f"{i}: {u}")
