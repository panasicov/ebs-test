# Generated by Django 4.2.4 on 2023-08-15 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_wishlist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='wishlist',
            new_name='wishlists',
        ),
    ]