# Generated by Django 4.1 on 2022-10-28 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_alter_forumumkm_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='replies',
            name='user',
            field=models.IntegerField(),
        ),
    ]