# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-14 05:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0035_serviceorder_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='serviceorder',
            name='tax_amount',
            field=models.FloatField(default=0, verbose_name='iva'),
        ),
        migrations.AddField(
            model_name='serviceorder',
            name='total_amount',
            field=models.FloatField(default=0, verbose_name='total de la reparacion'),
        ),
        migrations.AddField(
            model_name='serviceorder',
            name='total_final',
            field=models.FloatField(default=0, verbose_name='total con iva'),
        ),
    ]
