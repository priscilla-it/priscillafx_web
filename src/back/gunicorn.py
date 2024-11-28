"""This code is licensed under the GPL-3.0 license
Written by masajinobe-ef
"""

import multiprocessing

# Server settings
bind = '127.0.0.1:8000'

# Adjust by CPU
workers = (2 * multiprocessing.cpu_count()) + 1
worker_class = 'uvicorn.workers.UvicornWorker'

# Load app before worker, faster startup, but slow reload.
preload_app = True

# Run Gunicorn as a daemon or attached on terminal
daemon = False

# Timeout settings
timeout = 60
keepalive = 5

# Additional settings
max_requests = 1000
max_requests_jitter = 100

# Logging
accesslog = '-'
errorlog = '-'
loglevel = '-'
