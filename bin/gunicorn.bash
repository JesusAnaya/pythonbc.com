#!/bin/bash

/home/python/pythonbc/venv/bin/gunicorn config.wsgi -c /home/python/pythonbc/bin/gunicorn.conf.py
