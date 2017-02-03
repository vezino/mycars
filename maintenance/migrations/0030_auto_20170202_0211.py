# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-02 02:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0029_auto_20170127_0704'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceordertotal',
            name='spare_parts',
            field=models.FloatField(default=0, verbose_name='precio refacciones'),
        ),
        migrations.AddField(
            model_name='serviceordertotal',
            name='workforce',
            field=models.FloatField(default=0, verbose_name='mano de obra'),
        ),
    ]
