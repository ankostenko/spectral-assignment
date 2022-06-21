FROM python:3.7.5-slim-buster

ENV INSTALL_PATH /spectral
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt 
RUN pip install -r requirements.txt

COPY --from=protos generated /spectral/spectral/gen_grpc

COPY . .

RUN pip install --editable .

CMD python spectral/app.py
