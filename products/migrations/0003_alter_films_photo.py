# Generated by Django 4.2.8 on 2023-12-19 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_films_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='films',
            name='photo',
            field=models.ImageField(blank=True, upload_to='static/image'),
        ),
    ]
