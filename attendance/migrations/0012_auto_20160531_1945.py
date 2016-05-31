# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-31 19:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0011_delete_usermethods'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectSeparation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_spend', models.DurationField()),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.Project')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attendance.Session')),
            ],
        ),
        migrations.AddField(
            model_name='session',
            name='project',
            field=models.ManyToManyField(through='attendance.ProjectSeparation', to='attendance.Project'),
        ),
    ]