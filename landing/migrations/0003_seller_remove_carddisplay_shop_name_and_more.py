# Generated by Django 4.1 on 2022-10-26 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0002_rename_desc_carddisplay_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='carddisplay',
            name='shop_name',
        ),
        migrations.AddField(
            model_name='carddisplay',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='landing.seller'),
        ),
    ]
