# Generated by Django 4.1 on 2022-10-29 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addkategori', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kategori',
            name='file_url',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='kategori',
            name='gambar',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]