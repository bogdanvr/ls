# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-02 09:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ls', '0005_auto_20180502_0943'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ourworks',
            options={'verbose_name': '\u0420\u0430\u0431\u043e\u0442\u0443', 'verbose_name_plural': '\u041d\u0430\u0448\u0438 \u0440\u0430\u0431\u043e\u0442\u044b'},
        ),
        migrations.RenameField(
            model_name='ourworks',
            old_name='service',
            new_name='name',
        ),
    ]