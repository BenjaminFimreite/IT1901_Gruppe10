# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-04 08:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fpro', '0010_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='ticketPrice',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=30),
        ),
    ]
