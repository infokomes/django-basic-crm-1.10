# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-09 19:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_auto_20161009_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='zipcode',
            field=models.CharField(blank=True, max_length=6, null=True, verbose_name='Zipcode'),
        ),
    ]