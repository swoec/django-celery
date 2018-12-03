# -*- coding: utf-8 -*-
from datetime import timedelta
from celery.schedules import crontab

BOKER = 'redis://localhost:6379/1'
result_backend = 'redis://localhost:6379/2'

CELERY_IMPORTS = (
	'celery_app.task1',
	'celery_app.task2',
	)

CELERY_TIMEZONE = 'Pacific/Auckland'

CELERYBEAT_SCHEDULE = {
	'task1' : {
		'task' : 'celery_app.task1.add',
		'schedule': timedelta(seconds=10),
		'args': (7,7)
	},
	'task2':{
		'task':'celery_app.task2.multipy',
		'schedule':crontab(hour=21,minute=05),
		'args': (8,9)
	}
}