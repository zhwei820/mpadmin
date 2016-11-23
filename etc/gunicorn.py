#!/usr/bin/env python
# coding=utf-8
"""
gunicorn 启动配置

__created__ = '9/12/2015'
__author__ = 'deling.ma'
"""

import gevent.monkey
import multiprocessing

gevent.monkey.patch_all()

bind = '0.0.0.0:8080'
max_requests = 10000
keepalive = 5

proc_name = 'cmdb'

workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'gunicorn.workers.ggevent.GeventWorker'

loglevel = 'info'
timeout = 90
errorlog = '-'

x_forwarded_for_header = 'X-FORWARDED-FOR'