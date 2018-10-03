# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from contact.models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('phone', 'mail', 'address')
admin.site.register(Contact, ContactAdmin)