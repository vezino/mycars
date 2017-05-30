# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-25 01:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uber', '0008_vmycarsincomebyyearmonth'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadUberData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='nombre de la carga')),
                ('fiel_procesed', models.BooleanField(default=False, verbose_name='activo')),
                ('uber_file_uploaded', models.ImageField(default='', upload_to='uber/uberfiles', verbose_name='archivo de datos de uber')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='fecha de alta')),
                ('last_modified', models.DateTimeField(auto_now=True, verbose_name='ultima modificacion')),
            ],
            options={
                'ordering': ['created_at'],
                'verbose_name_plural': 'Uber Data Load',
            },
        ),
    ]