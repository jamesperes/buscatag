# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-12 21:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buscatag', '0009_auto_20170112_1924'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projetolist',
            name='devs',
        ),
        migrations.RemoveField(
            model_name='projetolist',
            name='tag',
        ),
    ]
