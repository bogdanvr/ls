# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from about.models import About
from about.models import AboutImage

# Register your models here.
class AboutAdmin(admin.ModelAdmin):
    list_display = ('name', 'text')
admin.site.register(About, AboutAdmin)

class AboutImageAdmin(admin.ModelAdmin):
	list_display = ('image',)
admin.site.register(AboutImage, AboutImageAdmin)

