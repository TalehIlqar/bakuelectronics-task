FROM python:3.10-slim
ENV PYTHONUNBUFFERED 1

ENV APP_ROOT /code
ENV DEBUG False

RUN mkdir /code;

RUN apt-get update && \
    apt-get install -y \
        unzip \
        libglib2.0-0 \
        libnss3 \
        libgconf-2-4 \
        libfontconfig \
        wget \
        gnupg \
        gcc

WORKDIR ${APP_ROOT}

RUN mkdir /config
ADD requirements.txt /config/
RUN pip install --no-cache-dir -r /config/requirements.txt

ADD . ${APP_ROOT}