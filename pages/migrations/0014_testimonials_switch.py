# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-09 14:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0013_auto_20170209_1150'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonials',
            name='switch',
            field=models.BooleanField(default=False, verbose_name='Опубликовать'),
            preserve_default=False,
        ),
    ]
