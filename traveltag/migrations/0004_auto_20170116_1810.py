# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-16 18:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traveltag', '0003_auto_20170112_0336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tagcard',
            name='card_number',
            field=models.CharField(max_length=30, unique=True, verbose_name='Numero de TAG'),
        ),
    ]