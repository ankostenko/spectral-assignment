# Append grpc folder to path to avoid fixing absolute imports in generated grpc files
import os
import sys

CURR_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(CURR_DIR + '/gen_grpc')

# Actual program
from grpc_server import run
run()