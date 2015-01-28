#!/bin/bash

ROOT_PATH=/home/anaya
HOME_PATH=$ROOT_PATH/pythonbc

. $ROOT_PATH/.bash_profile

$HOME_PATH/venv/bin/gunicorn config.wsgi -c $HOME_PATH/bin/gunicorn.conf.py
