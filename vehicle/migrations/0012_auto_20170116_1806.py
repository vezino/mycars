# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-16 18:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0011_auto_20170116_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicleassigment',
            name='traveltag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicleassigment1', to='traveltag.Tagcard', verbose_name='TAG'),
        ),
    ]
