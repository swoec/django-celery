import djcelery
from datetime import timedelta

djcelery.setup_loader()

CELERY_IMPORTS = (
	'cource.task',
	)

CELERY_QUEUES = {
	'beat_tasks' :{
		'exchange':'beat_tasks',
		'exchange_type':'direct',
		'binding_key':'beat_tasks'
	},
	'work_queue' :{
		'exchange':'work_queue',
		'exchange_type':'direct',
		'binding_key':'work_queue'
	},
}

CELERY_DEFAULT_QUEUE = 'work_queue'
# avoid deadlock
CELERYD_FORCE_EXECV = True 

#prallel 

CELERYD_CONCURRENCY = 4

CELERY_ACKS_LATE = True

#how many tasks every worker
CELERYD_MAX_TASKS_PER_CHILD = 100

#timeout every task time limit
CELERYD_TASK_TIME_LIMIT = 12 * 30

CELERYBEAT_SCHEDULE = {
	'task1': {
		'task': 'cource-task',
		'schedule':timedelta(seconds=5),
		'options': {
			'queue': 'beat_tasks'
			}
		}
	}
	
