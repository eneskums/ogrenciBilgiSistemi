# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2020-05-02 01:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('content', models.TextField()),
                ('published_time', models.DateField(auto_now_add=True)),
                ('Ders', models.CharField(default='', max_length=120, verbose_name='Ders')),
                ('Not', models.TextField(default='', verbose_name='Not')),
                ('Sınıf', models.CharField(default='', max_length=120, verbose_name='Sınıf')),
                ('Yükleyen', models.CharField(default='', max_length=150, verbose_name='Yükleyen')),
                ('pdf', models.FileField(blank=True, null=True, upload_to='')),
                ('yukleyenId', models.EmailField(max_length=254)),
            ],
            options={
                'ordering': ['-published_time', 'id'],
            },
        ),
    ]
