# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-13 15:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_auto_20170206_1657'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, upload_to='static/upload/news/', verbose_name='Картинка'),
        ),
    ]
