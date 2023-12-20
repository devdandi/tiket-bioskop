# Generated by Django 4.2.8 on 2023-12-20 04:50

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_films_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilmSchedules',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('schedule', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.films')),
            ],
        ),
    ]
