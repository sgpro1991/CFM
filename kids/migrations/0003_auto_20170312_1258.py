# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-12 12:58
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kids', '0002_auto_20170312_1239'),
    ]

    operations = [
        migrations.CreateModel(
            name='Programs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название программы')),
                ('response', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Содержание')),
            ],
            options={
                'verbose_name_plural': 'Программы',
            },
        ),
        migrations.AlterField(
            model_name='sliderkids',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/static/upload/slider-kids/', verbose_name='Файл'),
        ),
    ]