# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-14 04:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0005_auto_20170126_0204'),
    ]

    operations = [
        migrations.DeleteModel(
            name='GasCardUsage',
        ),
    ]
