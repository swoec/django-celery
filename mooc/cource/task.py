
from celery.task import Task
import time


class CourceTask(Task):

	name = 'cource-task'

	def run(self, *args, **kwargs):
		print('-------start-------')
		time.sleep(4)
		#print('end')
