# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-16 19:05
from __future__ import unicode_literals

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('talent', '0002_auto_20170416_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musician',
            name='instruments',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='talent.InstrumentTag', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]