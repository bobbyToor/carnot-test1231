"""Gunicorn *development* config file"""

wsgi_app = "carnot.wsgi:application"
loglevel = "debug"
workers = 2
bind = "0.0.0.0:8000"
reload = True
capture_output = True
daemon = False
