# Generated by Django 2.2.12 on 2020-05-09 23:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_auto_20200510_0211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mezun',
            name='ogrenciNo',
        ),
    ]
