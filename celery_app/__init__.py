# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 18:03:53 2017

@author: alex
"""

#from celery import Celery

from celery import Celery
#broker = 'redis://localhost:6379/1'
#backend = 'redis://localhost:6379/2'
app = Celery('demo')


app.config_from_object('celery_app.celeryconfig')
