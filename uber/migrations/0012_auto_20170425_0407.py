# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-25 04:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uber', '0011_auto_20170425_0214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploaduberdata',
            name='fiel_procesed',
            field=models.NullBooleanField(default=False, verbose_name='Procesado'),
        ),
    ]
