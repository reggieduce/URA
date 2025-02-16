# Generated by Django 5.0.10 on 2025-01-30 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rentals", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="rentalproperty",
            name="property_type",
            field=models.CharField(
                choices=[("residential", "Residential"), ("penwell", "Penwell")],
                default="residential",
                max_length=20,
            ),
        ),
    ]
