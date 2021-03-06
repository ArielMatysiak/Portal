# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-07-06 09:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classifieds', '0006_auto_20170705_1951'),
    ]

    operations = [
        migrations.CreateModel(
            name='BandComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Komentarz')),
                ('author', models.CharField(blank=True, max_length=255, verbose_name='Autor')),
                ('band', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classifieds.Band')),
            ],
        ),
    ]
