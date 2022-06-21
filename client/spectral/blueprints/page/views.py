from flask import Blueprint, render_template, jsonify

import grpc
from spectral.gen_grpc.meterusage_pb2_grpc import MeterUsageStub
from spectral.gen_grpc.meterusage_pb2 import UsageRequest

page = Blueprint('page', __name__, template_folder='templates')


@page.route('/')
def home():
    """
        Renders home page
    """
    return render_template('page/home.html')


@page.route('/request_data', methods=['GET'])
def request_data():
    """
        Requests meterusage data from server
    """
    # Connect to grpc server and retrieve usage data
    with grpc.insecure_channel('grpc_server:50051') as channel:
        stub = MeterUsageStub(channel)
        response = stub.GetUsageData(UsageRequest(
                                            usage_stat_name='meterusage'))
        return jsonify({"datetime": list(response.datetime),
                        "values": list(response.usage)})
