# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Contact(models.Model):
	phone = models.CharField(max_length = 50, unique = False, db_index = True, verbose_name = "Телефон")
	mail = models.CharField(max_length = 50, unique = False, db_index = True, verbose_name = "Email")
	address = models.CharField(max_length = 50, unique = False, db_index = True, verbose_name = "Адрес")
	
	class Meta:
		verbose_name="Контакт"
		verbose_name_plural="Контакты"
	
	
	


