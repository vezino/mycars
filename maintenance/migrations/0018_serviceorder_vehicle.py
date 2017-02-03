# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-27 04:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0015_auto_20170116_1819'),
        ('maintenance', '0017_remove_serviceorder_vehicle'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceorder',
            name='vehicle',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='maintenceserviceorder', to='vehicle.Vehicle', verbose_name='vehiculo'),
            preserve_default=False,
        ),
    ]