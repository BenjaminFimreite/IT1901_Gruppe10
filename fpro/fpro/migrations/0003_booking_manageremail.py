# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-27 09:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fpro', '0002_auto_20170923_1405'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='managerEmail',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
