# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-12 12:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0023_auto_20170312_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/static/upload/slider/', verbose_name='Файл'),
        ),
    ]