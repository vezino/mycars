# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-02 02:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0031_auto_20170202_0228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceordertotal',
            name='service_item_price',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maintenance.ServiceItem', verbose_name='Descripcion del trabajo'),
        ),
    ]