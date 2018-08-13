#!/usr/bin/env python3
import logging.config
import os

from flask import Flask, request, jsonify
from flask_graphql import GraphQLView


from service.graphql.graphql_schema import schema

FLASK_ENV = os.getenv('FLASK_ENV')
if not FLASK_ENV: raise ValueError('FLASK_ENV not set!')


# Create App
def create_app():
    app = Flask(__name__, instance_relative_config=True)

    # Configure Logger
    logging.config.fileConfig('gunicorn-logging.conf')
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.DEBUG)

    # Configure App
    app.config.from_object('config.default')
    app.config.from_object('config.' + FLASK_ENV)
    APP_CONFIG_FILE = os.getenv('APP_CONFIG_FILE')
    if APP_CONFIG_FILE is not None:
        app.config.from_envvar(APP_CONFIG_FILE, silent=True)

    app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

    return app

graphql_app = create_app()


if __name__ == "__main__":
    graphql_app.run(debug = graphql_app.config['DEBUG'])

