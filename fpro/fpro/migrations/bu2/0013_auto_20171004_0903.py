# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-04 09:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fpro', '0012_auto_20171004_0852'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='band',
            name='Genre',
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
    ]
