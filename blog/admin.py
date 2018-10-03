# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from blog.models import Blog, Category

class BlogAdmin(admin.ModelAdmin):
    list_display = ('category', 'name', 'date_post')
    class Media:
        js = (
            '/static/tiny_mce/tinymce.min.js',
            '/static/tiny_mce/tiny_mce_init.js',
        )
admin.site.register(Blog, BlogAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
admin.site.register(Category, CategoryAdmin)
