# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-21 03:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180620_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date_post',
            field=models.DateField(default=datetime.date(2018, 6, 21), verbose_name='\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f \u0441\u0442\u0430\u0442\u044c\u0438'),
        ),
    ]