# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-27 10:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fpro', '0003_bandinfo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bandinfo',
            name='band',
        ),
        migrations.DeleteModel(
            name='BandInfo',
        ),
    ]
