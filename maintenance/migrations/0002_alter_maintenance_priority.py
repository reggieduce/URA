# Generated by Django 5.0.10 on 2025-02-16 00:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maintenance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintenance',
            name='priority',
            field=models.CharField(choices=[('Low', 'low'), ('Medium', 'medium'), ('High', 'high'), ('Urgent', 'urgent')], default='Medium', max_length=10),
        ),
    ]
