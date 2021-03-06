# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-23 14:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('fpro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='scene',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='fpro.Scene'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='technicalRequirements',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.RemoveField(
            model_name='booking',
            name='technicians',
        ),
        migrations.AddField(
            model_name='booking',
            name='technicians',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
