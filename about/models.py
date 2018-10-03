# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class About(models.Model):
  name = models.CharField(max_length = 150, unique = True, db_index = True, verbose_name = "Заголовок")
  text = models.TextField(verbose_name = "О компании")
  

  def __unicode__(self):
        return self.name
  class Meta:
        verbose_name="О компании"
        verbose_name_plural="О компании"
        
        
class AboutImage(models.Model):
	image = models.ImageField(upload_to = 'about_slider', verbose_name = 'Изображение слайдера')
	alt = models.CharField(max_length = 150, unique = True, db_index = True, verbose_name = 'Описание изображения')
	
	def __unicode__(self):
		return self.alt
	class Meta:
		verbose_name = "Изображение"
		verbose_name_plural = "Изображения слайдера"
	