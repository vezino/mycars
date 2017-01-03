# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-03 01:48
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='nombre/s')),
                ('last_name', models.CharField(max_length=100, verbose_name='apellidos')),
                ('birthdate', models.DateTimeField(default=datetime.datetime.now, verbose_name='fecha de nacimiento')),
                ('license_type', models.CharField(choices=[('0', 'N/A'), ('A', 'TIPO A '), ('B', 'TIPO B'), ('C', 'TIPO C'), ('D', 'TIPO D')], default=0, max_length=1, verbose_name='tipo de licencia')),
                ('license_number', models.CharField(max_length=100, verbose_name='numero de licencia')),
                ('license_valid', models.DateTimeField(default=datetime.datetime.now, verbose_name='fecha de vencimiento')),
                ('blod_type', models.CharField(choices=[('0', 'N/A'), ('1', 'O-'), ('2', 'O+'), ('3', 'A-'), ('4', 'A+'), ('5', 'B-'), ('6', 'B+'), ('7', 'AB-'), ('8', 'AB+')], default=0, max_length=1, verbose_name='tipo de sangre')),
                ('created_at', models.DateTimeField(default=datetime.datetime.now, verbose_name='fecha de alta')),
                ('status', models.CharField(choices=[('0', 'N/A'), ('1', 'activo'), ('2', 'inactivo')], default=0, max_length=1, verbose_name='tipo de sangre')),
            ],
            options={
                'verbose_name_plural': 'choferes',
            },
        ),
    ]