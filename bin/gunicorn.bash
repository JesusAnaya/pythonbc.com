#!/bin/bash

HOME_PATH=/home/python/pythonbc

$HOME_PATH/venv/bin/gunicorn config.wsgi -c $HOME_PATH/bin/gunicorn.conf.py
