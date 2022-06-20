FROM python:3.7.5-slim-buster

ENV INSTALL_PATH /spectral
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

RUN python -m pip install grpcio
RUN python -m pip install grpcio-tools

COPY --from=protos generated /spectral/spectral/gen_grpc

COPY . .

CMD python spectral/app.py
