# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-28 22:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('identificacion', '0006_auto_20160428_2202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='type',
            name='identify',
        ),
        migrations.AddField(
            model_name='identify',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='identificacion.Type'),
        ),
    ]
