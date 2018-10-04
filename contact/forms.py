#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django import forms
from django.core.mail import send_mail, BadHeaderError


class ContactForm(forms.Form):
	subject = forms.CharField(max_length = 100, widget = forms.TextInput(attrs = {'class': 'form-control'}))
	sender = forms.EmailField(widget = forms.EmailInput(attrs = {'class': 'form-control'}))
	message = forms.CharField(widget = forms.TextInput(attrs = {'class': 'form-control'}))
	copy = forms.BooleanField(required = False)