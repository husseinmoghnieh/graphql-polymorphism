FROM python:3.6-slim

RUN pip install gunicorn json-logging-py
RUN pip install honcho

COPY . /graphql
WORKDIR /graphql
RUN mkdir /graphql/logs
ENV FLASK_APP=./app.py

RUN pip install -r requirements.txt

ENTRYPOINT ["/usr/local/bin/honcho", "start"]
