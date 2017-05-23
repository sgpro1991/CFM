# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-07 17:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0018_auto_20170306_1711'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(choices=[('1', 'Екатеринбург'), ('2', 'Курган'), ('3', 'Магнитогорск'), ('4', 'Челябинск')], max_length=255, verbose_name='Филиал')),
                ('small_image', models.ImageField(upload_to='static/upload/Photos/small/', verbose_name='Превью')),
                ('big_image', models.ImageField(upload_to='static/upload/Photos/big/', verbose_name='Оригинал')),
                ('title', models.CharField(blank=True, max_length=255, verbose_name='Подпись картинки')),
            ],
        ),
    ]
