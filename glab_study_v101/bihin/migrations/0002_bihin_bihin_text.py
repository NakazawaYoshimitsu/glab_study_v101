# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-03 22:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bihin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bihin',
            name='bihin_text',
            field=models.TextField(null=True, verbose_name='付属品'),
        ),
    ]
