# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 21:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0017_auto_20170131_0141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='slug',
            field=models.SlugField(allow_unicode=True, editable=False, unique=True, verbose_name='Slug'),
        ),
    ]
