# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from ls.models import OurWorks, ServiceDetail, SubServices, Services

# Register your models here.
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('name', 'text', 'image')
admin.site.register(Services, ServicesAdmin)

class OurWorksAdmin(admin.ModelAdmin):
    list_display = ('name', 'text', 'image')
admin.site.register(OurWorks, OurWorksAdmin)

class ServiceDetailAdmin(admin.ModelAdmin):
    list_display = ('name', 'image') 
    class Media:
        js = (
            '/static/tiny_mce/tinymce.min.js',
            '/static/tiny_mce/tiny_mce_init.js',
        )
admin.site.register(ServiceDetail, ServiceDetailAdmin)

class SubServicesAdmin(admin.ModelAdmin):
    list_display = ('service', 'name', 'text', 'image')
admin.site.register(SubServices, SubServicesAdmin)