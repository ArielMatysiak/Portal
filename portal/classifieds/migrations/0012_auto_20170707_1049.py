# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-07-07 10:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classifieds', '0011_auto_20170707_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='band',
            name='image',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
