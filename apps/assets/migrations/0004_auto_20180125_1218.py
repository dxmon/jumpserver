# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-25 04:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0003_auto_20180109_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assetgroup',
            name='created_by',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='Created by'),
        ),
    ]