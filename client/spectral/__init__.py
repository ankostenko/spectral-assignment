import os
import sys

# Append grpc folder to path to avoid fixing absolute imports in generated grpc files
CURR_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(CURR_DIR + '/gen_grpc')