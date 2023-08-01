# Generated by Django 4.1.7 on 2023-07-12 03:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.BigIntegerField(null=True)),
                ('name', models.CharField(max_length=50, null=True)),
                ('type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.category')),
            ],
        ),
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=80)),
                ('venue', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.address')),
            ],
        ),
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_date', models.DateField(null=True)),
                ('created', models.DateField(auto_now=True)),
                ('deliver_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.address')),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.product')),
                ('ordered_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
