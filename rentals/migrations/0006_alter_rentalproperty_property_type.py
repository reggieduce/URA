# Generated by Django 5.0.10 on 2025-01-31 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rentals", "0005_alter_rentalproperty_property_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="rentalproperty",
            name="property_type",
            field=models.CharField(
                choices=[
                    ("residential", "Residential"),
                    ("penwell", "Penwell"),
                    ("airbnb", "Airbnb"),
                    ("commercial", "Commercial"),
                ],
                default="residential",
                max_length=20,
            ),
        ),
    ]
