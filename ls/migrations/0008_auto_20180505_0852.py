# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-05 08:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ls', '0007_ourworks_alt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ourworks',
            name='alt',
            field=models.CharField(db_index=True, max_length=50, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0434\u043b\u044f \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f'),
        ),
        migrations.AlterField(
            model_name='ourworks',
            name='image',
            field=models.ImageField(upload_to='works', verbose_name='\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435'),
        ),
        migrations.AlterField(
            model_name='ourworks',
            name='text',
            field=models.TextField(verbose_name='\u0412\u0441\u043f\u043b\u044b\u0432\u0430\u044e\u0449\u0435\u0435 \u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0432\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u043e\u0439 \u0443\u0441\u043b\u0443\u0433\u0438'),
        ),
    ]