# Generated by Django 5.1.5 on 2025-01-21 11:03

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalog',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='catalog',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
