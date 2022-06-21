from concurrent import futures
import logging

import grpc
from gen_grpc.meterusage_pb2 import UsageReply
from gen_grpc.meterusage_pb2_grpc import MeterUsageServicer, add_MeterUsageServicer_to_server

from db.db_mock import get_usage_data

class MeterUsageServer(MeterUsageServicer):

    def GetUsageData(self, request, context):
        datetime, values = get_usage_data(request.usage_stat_name)
        return UsageReply(datetime=datetime, usage=values)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    add_MeterUsageServicer_to_server(MeterUsageServer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

def run():
    logging.basicConfig()
    serve()