# Generated by Django 4.1 on 2022-10-27 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0008_alter_carddisplay_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='carddisplay',
            name='file_url',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='carddisplay',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]