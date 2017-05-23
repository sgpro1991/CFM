# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 09:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_doctors_email'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='doctors',
            options={'verbose_name_plural': 'Наши специалисты'},
        ),
        migrations.AddField(
            model_name='doctors',
            name='image4',
            field=models.ImageField(blank=True, upload_to='static/upload/Doctors/520/', verbose_name='Дополнительная картинка 520 Х 660'),
        ),
    ]