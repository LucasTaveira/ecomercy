# Generated by Django 4.1.2 on 2022-10-26 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_product_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=models.ImageField(upload_to='media/product/pictures/', verbose_name='Foto produto'),
        ),
    ]
