# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-10-16 07:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bihin', '0013_auto_20161016_1610'),
    ]

    operations = [
        migrations.AddField(
            model_name='bihin',
            name='bihin_ipaddr',
            field=models.CharField(blank=True, max_length=255, verbose_name='IPアドレス'),
        ),
    ]
