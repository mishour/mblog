# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-19 07:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20160518_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='summary',
            field=models.CharField(max_length=1000),
        ),
    ]
