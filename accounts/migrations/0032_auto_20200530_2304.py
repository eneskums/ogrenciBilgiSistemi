# Generated by Django 2.2.12 on 2020-05-30 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0031_auto_20200530_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ogrenci',
            name='ogrenciNo',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]