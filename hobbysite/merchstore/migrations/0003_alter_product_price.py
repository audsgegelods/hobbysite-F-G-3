# Generated by Django 5.1.6 on 2025-03-05 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('merchstore', '0002_alter_product_options_alter_producttype_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=999999999),
        ),
    ]
