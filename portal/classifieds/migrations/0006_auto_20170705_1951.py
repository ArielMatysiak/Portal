# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-07-05 19:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classifieds', '0005_band_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='video',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='band',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]