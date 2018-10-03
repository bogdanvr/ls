# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime



class Category(models.Model):
	name = models.CharField(max_length = 150, unique = True, db_index = True, verbose_name = "Название категории")
	short_text = models.TextField(max_length = 72, verbose_name = "Краткое описание")
	
	def __unicode__(self):
		return self.name
	class Meta:
		verbose_name="Категорию"
		verbose_name_plural="Категории"



class Blog(models.Model):
	category = models.ForeignKey(Category, verbose_name = "Категория")
	name = models.CharField(max_length = 150, unique = True, db_index = True, verbose_name = "Название статьи")
	short_text = models.TextField(max_length = 500, verbose_name = "Краткое описание")
	image = models.ImageField(upload_to = "blog", verbose_name = "Изображение")
	full_text = models.TextField(max_length = 10000, verbose_name = "Полное описание")
	date_post = models.DateField(default=datetime.date.today(), verbose_name = "Дата создания статьи")
	
	class Meta:
		verbose_name="Статью"
		verbose_name_plural="Статьи"
		


		