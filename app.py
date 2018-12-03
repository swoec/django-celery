# -*- coding: utf-8 -*-

import time
from celery_app import task1
from celery_app import task2

task1.add.delay(5,5)
task2.multipy.delay(5,5)




