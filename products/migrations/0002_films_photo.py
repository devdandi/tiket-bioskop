# Generated by Django 4.2.8 on 2023-12-19 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='films',
            name='photo',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
