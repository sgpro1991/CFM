# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-04 13:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20170204_0909'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='slider',
            options={'verbose_name': 'Слайдер главной страницы'},
        ),
        migrations.AlterField(
            model_name='slider',
            name='image',
            field=models.ImageField(blank=True, upload_to='static/upload/slider/', verbose_name='Файл'),
        ),
    ]
