# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-30 05:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_planner', '0004_auto_20160430_0517'),
    ]

    operations = [
        migrations.AddField(
            model_name='requirementsource',
            name='name',
            field=models.CharField(default='NAME', max_length=100),
            preserve_default=False,
        ),
    ]
