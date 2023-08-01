# Generated by Django 4.1.7 on 2023-07-15 04:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0008_product_desc_product_images_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='ordered_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
