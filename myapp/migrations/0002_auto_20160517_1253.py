# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-17 12:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='article',
            name='summary',
            field=models.CharField(max_length=100),
        ),
    ]
