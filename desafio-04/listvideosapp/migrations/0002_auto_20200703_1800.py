# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-07-03 18:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listvideosapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.CharField(max_length=500),
        ),
    ]
