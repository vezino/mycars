# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-27 04:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0018_serviceorder_vehicle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serviceorder',
            name='vehicle',
        ),
    ]
