# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-09-11 06:13
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180621_0323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date_post',
            field=models.DateField(default=datetime.date(2018, 9, 11), verbose_name='\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f \u0441\u0442\u0430\u0442\u044c\u0438'),
        ),
    ]
