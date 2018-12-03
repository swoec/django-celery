# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from cource.task import CourceTask
from django.http import HttpResponse
from django.http import JsonResponse


# Create your views here.

def do(request):
	#CourceTask.delay()
	print('-------do-------')
	CourceTask.apply_async(args=('hello',),queue = 'work-queue')

	return JsonResponse({'result':'OK'}) 


