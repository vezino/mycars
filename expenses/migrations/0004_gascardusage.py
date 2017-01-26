# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-25 19:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0003_auto_20170118_0301'),
    ]

    operations = [
        migrations.CreateModel(
            name='GasCardUsage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(default='', max_length=50)),
                ('date_usage', models.DateField(default=datetime.datetime.now, verbose_name='fecha de carga')),
                ('time_usage', models.TimeField(default=datetime.datetime.now, verbose_name='hora de carga')),
                ('bin_number', models.CharField(default='', max_length=20)),
                ('owner_name', models.CharField(default='', max_length=100)),
                ('fuel_type', models.CharField(choices=[('0', 'Selecciona el tipo de gasolina'), ('Magna', 'Magna'), ('Premium', 'Premium'), ('Disel', 'Disel')], default='', max_length=7, verbose_name='tipo de combustible')),
                ('station_number', models.CharField(default='', max_length=6)),
                ('plate', models.CharField(default='', max_length=7)),
                ('kms', models.FloatField(default=0, verbose_name='kilometraje')),
                ('vehicle_description', models.CharField(default='', max_length=100)),
                ('serial_number', models.CharField(default='', max_length=20)),
                ('charge_date', models.DateField(default=datetime.datetime.now, verbose_name='fecha de cargo')),
                ('gas_liters', models.FloatField(default=0, verbose_name='litros')),
                ('gas_price', models.FloatField(default=0, verbose_name='precio x litro')),
                ('ieps', models.FloatField(default=0, verbose_name='ieps')),
                ('initial_balance', models.FloatField(default=0, verbose_name='balance inicial')),
                ('final_balance', models.FloatField(default=0, verbose_name='balance final')),
                ('gas_total_without_tax', models.FloatField(default=0, verbose_name='total')),
                ('commission_without_tax', models.FloatField(default=0, verbose_name='comision sin iva')),
                ('comission_tax', models.FloatField(default=0, verbose_name='iva comision')),
                ('rendimiento', models.FloatField(default=0, verbose_name='rendimiento')),
                ('id_tx', models.IntegerField(default=0, verbose_name='id tx')),
                ('card_status', models.CharField(default='', max_length=20, verbose_name='status de la tarjeta')),
                ('period', models.CharField(default='', max_length=20, verbose_name='periodo')),
                ('invoice_folio', models.CharField(default='', max_length=20, verbose_name='folio factura')),
                ('folio_tx', models.CharField(default='', max_length=20, verbose_name='folio tx')),
            ],
            options={
                'verbose_name_plural': 'Tarjeta gastos gasolina',
            },
        ),
    ]
