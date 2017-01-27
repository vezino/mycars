# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-27 05:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0023_auto_20170127_0517'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceItemPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('spare_parts', models.FloatField(default=0, verbose_name='precio refacciones')),
                ('workforce', models.FloatField(default=0, verbose_name='mano de obra')),
                ('service_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ServiceItemPrice', to='maintenance.ServiceItem', verbose_name='Trabajo')),
            ],
            options={
                'verbose_name_plural': 'importe del trabajo',
            },
        ),
        migrations.RemoveField(
            model_name='serviceorderprice',
            name='spare_parts',
        ),
        migrations.RemoveField(
            model_name='serviceorderprice',
            name='workforce',
        ),
        migrations.AddField(
            model_name='serviceorderprice',
            name='service_order_item',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='maintenance.ServiceItemPrice'),
            preserve_default=False,
        ),
    ]
