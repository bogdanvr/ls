from ls.models import OurWorks, Services, SubServices
from about.models import About, AboutImage
from contact.models import Contact
from django.shortcuts import get_object_or_404
from django.template.loader import get_template
from django import template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
from blog.models import Category, Blog

register = template.Library()

@register.inclusion_tag('tags/ourwork.html')
def ourwork():
	data = OurWorks.objects.all()
	return {'data':data}
	
@register.inclusion_tag('tags/about_text.html')
def about_text():
	data = About.objects.get()
	return {'data':data}
	
@register.inclusion_tag('tags/about_image.html')
def about_image(id):
	data = AboutImage.objects.get(pk=int(id))
	return {'data':data}
	
@register.inclusion_tag('tags/phone.html')
def contact_phone(id):
	data = Contact.objects.get(pk=int(id))
	return {'data':data}
	
@register.inclusion_tag('tags/phone.html')
def contact_phone(id):
	data = Contact.objects.get(pk=int(id))
	return {'data':data}

@register.inclusion_tag('tags/mail.html')
def contact_mail(id):
	data = Contact.objects.get(pk=int(id))
	return {'data':data}
	
@register.inclusion_tag('tags/address.html')
def contact_address(id):
	data = Contact.objects.get(pk=int(id))
	return {'data':data}
	
	
@register.inclusion_tag('tags/service.html')
def service_tag():
	data = Services.objects.all()
	return {'data':data}
	
@register.inclusion_tag('tags/subservice.html')
def subservice_tag():
	data = SubServices.objects.all()
	return {'data':data}

@register.inclusion_tag('tags/ourworkindetail.html')
def our_work_in_detail(id):
	data = Ourwork.objects.filter(name_id=id)
	return {'data':data}
	
@register.inclusion_tag('tags/blog_category.html')
def blog_category():
	data = Category.objects.all()
	return {'data':data}
	
@register.inclusion_tag('tags/blog_index.html')
def blog_index():
	data = Blog.objects.all().order_by('-date_post')[:3]
	return {'data':data}	
