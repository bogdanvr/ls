#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django import forms
from django.core.mail import send_mail, BadHeaderError



class ContactForm(forms.Form):
	full_name = forms.CharField(required=False, label="Имя")
	email = forms.EmailField(label="E-mail", error_messages={'invalid': 'Введите E-mail'})
	message = forms.CharField(label="Сообщение")
	honeypot = forms.CharField(required=False, label='for spam')
	