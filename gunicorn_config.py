# gunicorn_config.py

import multiprocessing

command = '/home/ben-24/Example_project/todo/.venv/bin/gunicorn'
pythonpath = '/home/ben-24/Example_project/todo'
bind = "0.0.0.0:8000"  # Address and port to bind to
# workers = multiprocessing.cpu_count() * 2 + 1  # Number of worker processes
workers = 1  # Number of worker processes