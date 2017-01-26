# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-16 18:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('traveltag', '0003_auto_20170112_0336'),
        ('vehicle', '0008_auto_20170113_0550'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicleassigment',
            name='traveltag',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='vehicleassigment', to='traveltag.Tagcard', verbose_name='TAG'),
        ),
        migrations.AlterField(
            model_name='vehicleassigment',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vehicleassigment', to='vehicle.Vehicle', verbose_name='vehiculo'),
        ),
    ]