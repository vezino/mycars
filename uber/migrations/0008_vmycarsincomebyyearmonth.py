# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-11 03:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uber', '0007_v_mycars_income_by_year_month'),
    ]

    operations = [
        migrations.CreateModel(
            name='VMycarsIncomeByYearMonth',
            fields=[
                ('trip_year', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('trip_month', models.IntegerField(default=0)),
                ('viajes', models.IntegerField(default=0)),
                ('total_payment', models.FloatField(default=0)),
            ],
            options={
                'ordering': ['trip_year'],
                'managed': False,
                'verbose_name_plural': 'Year Month Uber Data',
            },
        ),
    ]
