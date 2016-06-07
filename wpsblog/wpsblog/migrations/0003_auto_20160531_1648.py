# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-31 16:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wpsblog', '0002_naverpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='naverpost',
            name='content',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='naverpost',
            name='thumbnail_image_url',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='naverpost',
            name='title',
            field=models.TextField(default=None),
            preserve_default=False,
        ),
    ]