# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-05 08:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=150, unique=True, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('text', models.TextField(verbose_name='\u041e \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u0438')),
            ],
            options={
                'verbose_name': '\u0423\u0441\u043b\u0443\u0433\u0443',
                'verbose_name_plural': '\u0423\u0441\u043b\u0443\u0433\u0438',
            },
        ),
    ]
