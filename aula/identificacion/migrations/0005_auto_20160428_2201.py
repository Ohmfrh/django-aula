# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-28 22:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('identificacion', '0004_auto_20160428_0255'),
    ]

    operations = [
        migrations.RenameField(
            model_name='type',
            old_name='identify',
            new_name='idtype',
        ),
    ]