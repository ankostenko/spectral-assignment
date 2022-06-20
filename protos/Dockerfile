FROM python:3.7.5-slim-buster

RUN python -m pip install grpcio
RUN python -m pip install grpcio-tools

COPY . protos

RUN mkdir generated
RUN python -m grpc_tools.protoc -I=./protos --python_out=generated --grpc_python_out=generated ./protos/meterusage.proto
