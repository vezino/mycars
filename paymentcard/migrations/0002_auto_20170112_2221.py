# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-12 22:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paymentcard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentcard',
            name='card_number',
            field=models.CharField(default=0, max_length=20, unique=True, verbose_name='numero de tarjeta'),
        ),
    ]