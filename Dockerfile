FROM python:3.8-buster

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY ./requirements.txt /app/

RUN pip install --upgrade pip
RUN pip install -r ./requirements.txt

COPY . /app

RUN chgrp -R 0 /app && \
  chmod -R g+rwX /app