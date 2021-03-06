# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-02 19:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(max_length=30)),
                ('start_at', models.DateTimeField(default=datetime.datetime.now)),
                ('end_at', models.DateTimeField(default=datetime.datetime.now)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company', to='insurances.Company')),
            ],
        ),
    ]
