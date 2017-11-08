# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-08 09:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fpro', '0012_booking_completedtechnicalrequirements'),
    ]

    operations = [
        migrations.RenameField(
            model_name='band',
            old_name='StreamCount',
            new_name='streamCount',
        ),
        migrations.RenameField(
            model_name='band',
            old_name='Visits',
            new_name='visits',
        ),
        migrations.AddField(
            model_name='band',
            name='albumSales',
            field=models.IntegerField(default=0),
        ),
    ]