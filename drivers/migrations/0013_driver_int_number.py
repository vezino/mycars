# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-12 03:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0012_auto_20170112_0323'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='int_number',
            field=models.CharField(blank=True, default='', max_length=20, verbose_name='n\xfamero interior'),
        ),
    ]