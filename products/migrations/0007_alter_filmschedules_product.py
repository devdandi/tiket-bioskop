# Generated by Django 4.2.8 on 2023-12-20 05:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_remove_filmschedules_film_schedules_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filmschedules',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.films'),
        ),
    ]
