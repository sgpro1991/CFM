# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-06 16:57
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20170204_1356'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('work', models.CharField(max_length=255, verbose_name='Специальность')),
                ('city', models.CharField(choices=[('1', 'Екатеринбург'), ('2', 'Курган'), ('3', 'Магнитогорск'), ('4', 'Челябинск')], max_length=255, verbose_name='Город')),
                ('text', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Информвция о докторе')),
                ('image1', models.ImageField(blank=True, upload_to='static/upload/Doctors/270/', verbose_name='Картинка 270 Х 270')),
                ('image2', models.ImageField(blank=True, upload_to='static/upload/Doctors/360/', verbose_name='Картинка 270 Х 360')),
                ('image3', models.ImageField(blank=True, upload_to='static/upload/Doctors/420/', verbose_name='Картинка 520 Х 660')),
            ],
        ),
        migrations.AlterModelOptions(
            name='slider',
            options={'verbose_name_plural': 'Слайдер главной страницы'},
        ),
    ]
