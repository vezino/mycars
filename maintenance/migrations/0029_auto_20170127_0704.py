# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-27 07:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0028_auto_20170127_0702'),
    ]

    operations = [
        migrations.RenameField(
            model_name='serviceordertotal',
            old_name='service_order',
            new_name='service_order_detail',
        ),
    ]
