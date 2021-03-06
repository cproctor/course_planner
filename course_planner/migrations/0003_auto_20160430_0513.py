# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-30 05:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_planner', '0002_auto_20160430_0256'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='requirement',
            options={'ordering': ('weight',)},
        ),
        migrations.AddField(
            model_name='requirement',
            name='weight',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='requirement',
            name='courses',
            field=models.ManyToManyField(related_name='requirements', to='course_planner.Course'),
        ),
    ]
