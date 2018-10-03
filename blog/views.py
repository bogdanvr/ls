# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.views.generic.list import ListView
from blog.models import Blog
from django.views.generic.detail import DetailView




class BlogView(ListView):
	model = Blog
	template_name = 'blog.html'
	context_object_name = 'blog_context'
	
class BlogDetailView(DetailView):
	model = Blog
	template_name = 'blogdetail.html'
	context_object_name = 'blog_detail_context'