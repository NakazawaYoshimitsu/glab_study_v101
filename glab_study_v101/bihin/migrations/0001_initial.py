# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-09-03 09:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bihin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bihin_no', models.CharField(max_length=255, verbose_name='No')),
                ('bihin_name', models.CharField(max_length=255, verbose_name='名称')),
                ('bihin_date', models.DateField(verbose_name='登録日')),
            ],
        ),
    ]
