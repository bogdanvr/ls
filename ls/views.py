# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from ls.models import Services, ServiceDetail
from ls.models import OurWorks
from django.shortcuts import render_to_response


class Main(ListView):
	template_name = "index.html"
	model = Services
	context_object_name = 'main'
	allow_empty = True
	allow_future = True
	

def servicedetail(request, service_id):
	args = {}
	args['name_context'] = ServiceDetail.objects.get(id=service_id)
	args['context_filter'] = OurWorks.objects.filter(name_id=service_id)
	return render_to_response('servicedetail.html', args)