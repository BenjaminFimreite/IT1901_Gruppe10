# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-03 07:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fpro', '0005_auto_20171003_0729'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='tacketsSold',
            new_name='ticketsSold',
        ),
    ]
