# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-19 08:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fpro', '0003_auto_20171005_1118'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='Songs',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
    ]
