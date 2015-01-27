#!/bin/bash
set -e

NUM_WORKERS=4

# user/group to run as
PORT=9900
HOST=0.0.0.0
APP_NAME=config.wsgi
GUNICORN_PATH=/var/lib/jenkins/workspace/pythonbc/venv/bin/gunicorn

cd /var/lib/jenkins/workspace/pythonbc
source ./venv/bin/activate


./venv/bin/python manage.py syncdb --settings=config.settings_production
./venv/bin/python manage.py migrate --all --settings=config.settings_production
./venv/bin/python manage.py collectstatic --noinput --settings=config.settings_production


$GUNICORN_PATH $APP_NAME -b $HOST:$PORT -w $NUM_WORKERS --log-level=debug
