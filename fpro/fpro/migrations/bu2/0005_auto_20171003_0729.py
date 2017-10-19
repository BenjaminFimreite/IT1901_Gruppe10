# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-03 07:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fpro', '0004_bandinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='bandPrice',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=30),
        ),
        migrations.AddField(
            model_name='booking',
            name='otherCosts',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=30),
        ),
        migrations.AddField(
            model_name='booking',
            name='tacketsSold',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='booking',
            name='ticketPrice',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=30),
        ),
    ]