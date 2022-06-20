from flask import Blueprint, render_template, jsonify

import grpc
from spectral.gen_grpc.meterusage_pb2_grpc import MeterUsageStub
from spectral.gen_grpc.meterusage_pb2 import HelloRequest

page = Blueprint('page', __name__, template_folder='templates')

@page.route('/')
def home():
    return render_template('page/home.html')

@page.route('/request_data', methods=['GET'])
def request_data():
    with grpc.insecure_channel('grpc_server:50051') as channel:
        stub = MeterUsageStub(channel)
        response = stub.SayHi(HelloRequest(name='Andrey'))
        print('Response: ', response)
    return jsonify({"hello": "world!"})