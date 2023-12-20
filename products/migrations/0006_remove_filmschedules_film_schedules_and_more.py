# Generated by Django 4.2.8 on 2023-12-20 05:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_rename_product_filmschedules_film_schedules'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filmschedules',
            name='film_schedules',
        ),
        migrations.AddField(
            model_name='filmschedules',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='film_schedules', to='products.films'),
        ),
    ]
