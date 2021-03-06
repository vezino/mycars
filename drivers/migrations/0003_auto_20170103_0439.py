# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-03 04:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0002_auto_20170103_0254'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='curp',
            field=models.CharField(default=0, max_length=18, verbose_name='CURP'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='email',
            field=models.CharField(default='', max_length=120, verbose_name='email'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='ext_number',
            field=models.CharField(default='', max_length=20, verbose_name='n\xfamero exterior'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='ife_number',
            field=models.CharField(default=0, max_length=20, verbose_name='IFE'),
        ),
        migrations.AlterField(
            model_name='driver',
            name='zip_code',
            field=models.CharField(default='', max_length=5, verbose_name='codigo postal'),
        ),
    ]
