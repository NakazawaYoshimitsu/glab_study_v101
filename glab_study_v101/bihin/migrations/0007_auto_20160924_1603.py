# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-24 07:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bihin', '0006_auto_20160924_1602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bihin',
            name='bihin_text',
            field=models.TextField(null=True, verbose_name='備考'),
        ),
    ]
