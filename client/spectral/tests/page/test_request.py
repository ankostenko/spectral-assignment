""" Tests request """

import grpc
from spectral.gen_grpc.meterusage_pb2_grpc import MeterUsageStub
from spectral.gen_grpc.meterusage_pb2 import UsageRequest


class TestRequest(object):
    def test_default_data_request(self, client):
        """
            Tests that default amount of data retrieved from server
        """
        # Connect to grpc server and retrieve usage data
        with grpc.insecure_channel('grpc_server:50051') as channel:
            stub = MeterUsageStub(channel)
            response = stub.GetUsageData(UsageRequest(
                                                usage_stat_name='meterusage'))
            assert len(list(response.datetime)) == 20


    def test_fifty_data_request(self, client):
        """
            Tests that default amount of data retrieved from server
        """
        # Connect to grpc server and retrieve usage data
        with grpc.insecure_channel('grpc_server:50051') as channel:
            stub = MeterUsageStub(channel)
            response = stub.GetUsageData(UsageRequest(
                                                usage_stat_name='meterusage',
                                                page_size=50))
            assert len(list(response.datetime)) == 50
