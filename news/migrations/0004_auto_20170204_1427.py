# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-04 14:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20170204_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='date_time',
            field=models.DateTimeField(editable=False, null=True, verbose_name='Дата время'),
        ),
    ]