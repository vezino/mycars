# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-27 04:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0013_auto_20170127_0344'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceorder',
            name='reparation',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='maintenceserviceorder', to='maintenance.ServiceItemPrice', verbose_name='reparacion'),
            preserve_default=False,
        ),
    ]
