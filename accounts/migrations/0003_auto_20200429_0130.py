# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2020-04-28 22:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_ogrenci_oncekigiris'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ogrenci',
            old_name='oncekiGiris',
            new_name='oncekiGirisIs',
        ),
        migrations.AddField(
            model_name='ogrenci',
            name='oncekiGirisStaj',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 28, 22, 30, 2, 688468, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
