# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-09 14:18
from __future__ import unicode_literals

import datetime
from django.conf import settings
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('musicians', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applause',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='GenreTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InstrumentTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Participation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instruments', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='performances.InstrumentTag', to='taggit.Tag', verbose_name='instruments')),
                ('musician', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicians.Musician')),
            ],
        ),
        migrations.CreateModel(
            name='Performance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('end_time', models.DateTimeField(default=datetime.datetime(2017, 6, 9, 14, 18, 50, 130755), null=True)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
                ('audience', models.ManyToManyField(null=True, through='performances.Applause', to=settings.AUTH_USER_MODEL)),
                ('genres', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='performances.GenreTag', to='taggit.Tag', verbose_name='genres')),
                ('musicians', models.ManyToManyField(null=True, through='performances.Participation', to='musicians.Musician')),
            ],
        ),
        migrations.AddField(
            model_name='participation',
            name='performance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='performances.Performance'),
        ),
        migrations.AddField(
            model_name='instrumenttag',
            name='content_object',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='performances.Participation'),
        ),
        migrations.AddField(
            model_name='instrumenttag',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='performances_instrumenttag_items', to='taggit.Tag'),
        ),
        migrations.AddField(
            model_name='genretag',
            name='content_object',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='performances.Performance'),
        ),
        migrations.AddField(
            model_name='genretag',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='performances_genretag_items', to='taggit.Tag'),
        ),
        migrations.AddField(
            model_name='applause',
            name='performance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='performances.Performance'),
        ),
        migrations.AddField(
            model_name='applause',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
