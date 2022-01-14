# Generated by Django 2.2.12 on 2020-05-15 22:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dersicerikMezun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.CharField(max_length=250)),
                ('soyad', models.CharField(max_length=250)),
                ('ogrenciNo', models.IntegerField(blank=True, null=True)),
                ('mezunYili', models.IntegerField()),
                ('telefon', models.CharField(max_length=11)),
                ('adres', models.TextField(max_length=250)),
                ('istekTarihi', models.DateTimeField()),
                ('teslimTarihi', models.DateTimeField()),
                ('mail', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='dersicerikOgrenci',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.CharField(max_length=250)),
                ('soyad', models.CharField(max_length=250)),
                ('ogrenciNo', models.IntegerField()),
                ('telefon', models.CharField(max_length=11)),
                ('adres', models.TextField(max_length=250)),
                ('istekTarihi', models.DateTimeField()),
                ('teslimTarihi', models.DateTimeField()),
                ('mail', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='MesajdersOgrenci',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.CharField(max_length=200)),
                ('mesaj', models.TextField()),
                ('belge', models.FileField(blank=True, null=True, upload_to='belgeler')),
                ('mesajTarihi', models.DateTimeField(auto_now_add=True)),
                ('dersicerik', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mesajOgrenci', to='dersicerik.dersicerikOgrenci')),
            ],
        ),
        migrations.CreateModel(
            name='MesajdersMezun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad', models.CharField(max_length=200)),
                ('mesaj', models.TextField()),
                ('belge', models.FileField(blank=True, null=True, upload_to='belgeler')),
                ('mesajTarihi', models.DateTimeField(auto_now_add=True)),
                ('dersicerik', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mesajMezun', to='dersicerik.dersicerikMezun')),
            ],
        ),
    ]