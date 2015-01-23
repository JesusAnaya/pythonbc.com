#!/bin/bash
set -e

LOGFILE=/home/python/pythonbc/gunicorn.log
LOGDIR=$(dirname $LOGFILE)
NUM_WORKERS=2

# user/group to run as
USER=python
GROUP=python
PORT=9900
IP=0.0.0.0
cd /home/python/pythonbc
source ./venv/bin/activate

exec /home/python/pythonbc/venv/bin/gunicorn_django -b $IP:$PORT -w $NUM_WORKERS \
  --user=$USER --group=$GROUP --log-level=debug --log-file=$LOGFILE 2>>$LOGFILE
