# Generated by Django 4.1.7 on 2023-07-14 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_product_for_sale'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='for_sale',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
