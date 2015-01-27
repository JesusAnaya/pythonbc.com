bind = '127.0.0.1:9900'
backlog = 2048
workers = 3
errorlog = '/home/python/pythonbc/gunicorn-error.log'
accesslog = '/home/python/pythonbc/gunicorn-access.log'
loglevel = 'debug'
proc_name = 'pythonbc'
pidfile = '/var/run/pythonbc.pid'
