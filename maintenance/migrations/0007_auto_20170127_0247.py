# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-27 02:47
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0006_auto_20170127_0238'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='serviceconcept',
            options={'ordering': ['name'], 'verbose_name_plural': 'concepto del servicio'},
        ),
        migrations.RenameField(
            model_name='serviceconcept',
            old_name='concept',
            new_name='name',
        ),
    ]