from concurrent import futures
import logging

import grpc
from gen_grpc.meterusage_pb2 import HelloReply
from gen_grpc.meterusage_pb2_grpc import MeterUsageServicer, add_MeterUsageServicer_to_server

class Greeter(MeterUsageServicer):
    def SayHi(self, request, context):
        return HelloReply(message='Hello, %s!' % request.name)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_MeterUsageServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

def run():
    logging.basicConfig()
    serve()