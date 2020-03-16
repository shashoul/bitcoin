FROM python:3.7.1-slim-stretch

ARG apikey

WORKDIR /bitcoin/

ADD . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

ENV apikey $apikey

ENTRYPOINT ["python","bitcoin.py"]