# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ckeditor.fields import RichTextField

class Services(models.Model):
  name = models.CharField(max_length = 150, unique = True, db_index = True, verbose_name = "Заголовок")
  text = models.TextField(verbose_name = "Краткое описание")
  image = models.ImageField(upload_to = "services", verbose_name = "Изображение")

  def __unicode__(self):
        return self.name
  class Meta:
        verbose_name="Услугу"
        verbose_name_plural="Услуги"
        
class SubServices(models.Model):
	service = models.ForeignKey(Services, verbose_name = "Услуга")
	name = models.CharField(max_length = 150, unique = True, db_index = True, verbose_name = "Заголовок")
	text = models.TextField(max_length = 72, verbose_name = "Краткое описание")
	image = models.ImageField(upload_to = "services", verbose_name = "Изображение")
	class Meta:
		verbose_name="Подуслугу"
		verbose_name_plural="Подуслуги"
        

class OurWorks(models.Model):
	name = models.ForeignKey(Services, verbose_name = "Категория")
	image = models.ImageField(upload_to = "works", verbose_name = "Выберите изображение")
	text = models.TextField(verbose_name = "Всплывающее описание выполненной услуги")
	alt = models.CharField(max_length = 50, unique = False, db_index = True, verbose_name = "Название для изображения")
	class Meta:
		verbose_name="Работу"
		verbose_name_plural="Наши работы"
		
class ServiceDetail(models.Model):
	name = models.ForeignKey(Services, verbose_name = "Услуга")
	header = models.CharField(max_length = 50, unique = False, db_index = True, verbose_name = "Заголовок")
	image = models.ImageField(upload_to = "services", verbose_name = "Выберите изображение")
	image2 = models.ImageField(upload_to = "services", verbose_name = "Выберите второе изображение ")
	image3 = models.ImageField(upload_to = "services", verbose_name = "Выберите третье изображение")
	text = models.TextField(verbose_name = "Текст описания услуги")
	text2 = models.TextField(verbose_name = "Второй абзац текста описания услуги")
	alt = models.CharField(max_length = 50, unique = False, db_index = True, verbose_name = "Название для изображения")
	class Meta:
		verbose_name="Страницу услуг"
		verbose_name_plural="Страницы услуг"

