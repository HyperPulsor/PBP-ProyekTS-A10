# Generated by Django 4.1 on 2022-10-31 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addproduct', '0002_remove_product_gambar_produk'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='gambar_produk',
            field=models.ImageField(default='', upload_to='images/'),
            preserve_default=False,
        ),
    ]
