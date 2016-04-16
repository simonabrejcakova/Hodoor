# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-16 11:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0004_auto_20160412_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='session',
            name='duration',
            field=models.DurationField(blank=True, null=True),
        ),
    ]