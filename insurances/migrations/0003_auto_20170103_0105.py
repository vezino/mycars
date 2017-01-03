# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-03 01:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurances', '0002_auto_20170103_0043'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name_plural': 'Compa\xf1ias'},
        ),
        migrations.AlterModelOptions(
            name='policy',
            options={'verbose_name_plural': 'Polizas'},
        ),
        migrations.AddField(
            model_name='policy',
            name='cover_amount',
            field=models.FloatField(default=0, verbose_name='importe de la coverura'),
        ),
        migrations.AddField(
            model_name='policy',
            name='price',
            field=models.FloatField(default=0, help_text='cuanto costo el seguro', verbose_name='importe del seguro'),
        ),
    ]
