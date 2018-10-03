# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic.base import TemplateView
from django.shortcuts import render
from about.models import About
from django.shortcuts import render_to_response




class AboutView(TemplateView):
	template_name = 'about.html'
	