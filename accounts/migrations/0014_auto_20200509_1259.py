# Generated by Django 2.2.12 on 2020-05-09 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20200508_0505'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bolumsekreteri',
            old_name='gorulenTranskript',
            new_name='gorulenTranskriptMezun',
        ),
        migrations.AddField(
            model_name='bolumsekreteri',
            name='gorulenTranskriptOgrenci',
            field=models.IntegerField(default=0),
        ),
    ]
