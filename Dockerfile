FROM python:3.7-alpine
LABEL maintainer="CHOU"

ENV PYTHONBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /fetus
WORKDIR /fetus
COPY ./fetus /fetus

RUN adduser -D user
USER user