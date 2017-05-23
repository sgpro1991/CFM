# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-24 16:52
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_newskids'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('image', models.ImageField(blank=True, upload_to='static/upload/news/', verbose_name='Картинка')),
                ('description', models.CharField(max_length=255, verbose_name='Описание')),
                ('date', models.DateTimeField(verbose_name='Дата время')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Текст')),
            ],
            options={
                'verbose_name_plural': 'Новости',
            },
        ),
        migrations.AlterModelOptions(
            name='newskids',
            options={'verbose_name_plural': 'Новости детское'},
        ),
    ]
