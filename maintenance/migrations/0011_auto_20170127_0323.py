# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-27 03:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0010_auto_20170127_0306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceitem',
            name='name',
            field=models.CharField(max_length=100, verbose_name='descripcion'),
        ),
    ]
