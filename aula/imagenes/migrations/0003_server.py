# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-30 22:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imagenes', '0002_auto_20160426_2155'),
    ]

    operations = [
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('user', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=500)),
            ],
        ),
    ]
