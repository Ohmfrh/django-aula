# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-28 02:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0010_auto_20160427_0208'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersys',
            name='email',
            field=models.CharField(default='a@a.a', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usersys',
            name='date_added',
            field=models.DateField(default=datetime.date(2016, 4, 28), verbose_name='Fecha de alta'),
        ),
    ]