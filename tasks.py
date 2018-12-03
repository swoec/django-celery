# -*- coding: utf-8 -*-
import time

from celery import Celery
broker = 'redis://localhost:6379/1'
backend = 'redis://localhost:6379/2'
app = Celery('my_tasks',broker=broker,backend=backend)

@app.task
def add(x, y):
	
    time.sleep(4)

    return x + y