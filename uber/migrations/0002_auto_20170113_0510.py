# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-13 05:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uber', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='uberdata',
            options={'ordering': ['trip_date'], 'verbose_name_plural': 'Uber Data'},
        ),
        migrations.RenameField(
            model_name='uberdata',
            old_name='date',
            new_name='trip_date',
        ),
    ]