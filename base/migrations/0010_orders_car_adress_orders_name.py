# Generated by Django 4.1.7 on 2023-07-15 04:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_orders_ordered_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='car_adress',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.cart'),
        ),
        migrations.AddField(
            model_name='orders',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.product'),
        ),
    ]
