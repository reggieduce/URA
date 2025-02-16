# Generated by Django 5.0.10 on 2025-01-30 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("rentals", "0002_rentalproperty_property_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="rentalproperty",
            name="bathrooms",
            field=models.DecimalField(decimal_places=1, default=1.0, max_digits=3),
        ),
        migrations.AddField(
            model_name="rentalproperty",
            name="is_available",
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name="rentalproperty",
            name="tenant_name",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="rentalproperty",
            name="tenant_phone",
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name="rentalproperty",
            name="zip_code",
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
