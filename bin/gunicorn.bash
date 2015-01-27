#!/bin/bash
set -e

NUM_WORKERS=4

# user/group to run as
PORT=9900
HOST=0.0.0.0
APP_NAME=config.wsgi
GUNICORN_PATH=/var/lib/jenkins/workspace/pythonbc/venv/bin/gunicorn

$GUNICORN_PATH $APP_NAME -b $HOST:$PORT -w $NUM_WORKERS --log-level=debug
