# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from django.shortcuts import render


from contact.forms import ContactForm
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from django.template import RequestContext
from django.conf import settings
from django.shortcuts import render_to_response, redirect





def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
    	if form.cleaned_data["honeypot"] == "":
    		
	        form_email = form.cleaned_data.get("email")
	        form_message = form.cleaned_data.get("message")
	        form_full_name = form.cleaned_data.get("full_name")
	        subject = 'Письмо с сайта OZNA.SU со страницы КОНТАКТЫ'
	        from_email = settings.EMAIL_HOST_USER
	        to_email = [from_email, 'bv2211@mail.ru']
	        contact_message = "(     Имя: %s     )_______(     Сообщение: %s     )_______(     E-mail: %s     )" %(
	            form_full_name,
	            form_message,
	            form_email)
	
	        send_mail(subject,
	        contact_message,
	        from_email,
	        to_email,
	        fail_silently=True)
	        return HttpResponseRedirect('/thanks/')
    context = {
        "form":form,
    }
    return render(request, "contact.html", context)
    
    
    
class ThanksView(TemplateView):
	template_name = "thanks.html"
	
