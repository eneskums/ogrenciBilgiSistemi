# Generated by Django 2.2.12 on 2020-05-07 05:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('belgeler', '0002_auto_20200503_0821'),
    ]

    operations = [
        migrations.CreateModel(
            name='MesajMezun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.CharField(max_length=200)),
                ('mesaj', models.TextField()),
                ('belge', models.FileField(blank=True, null=True, upload_to='')),
                ('mesajTarihi', models.DateTimeField(auto_now_add=True)),
                ('transkript', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mesajOgrenci', to='belgeler.TranskriptMezun')),
            ],
        ),
    ]
