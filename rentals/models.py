from django.db import models

# Create your models here.
class RentalProperty(models.Model):
    PROPERTY_TYPES = [
        ('residential', 'Residential'),
        ('penwell', 'Penwell'),
        ('airbnb', 'Airbnb'),
        ('commercial', 'Commercial')
    ]
    apt_number = models.CharField(max_length=255) 
    street_address = models.CharField(max_length=255)  # Property address
    is_available = models.BooleanField(default=True)
    tenant_name = models.CharField(max_length=255, null=True, blank=True)
    tenant_phone = models.CharField(max_length=15, null=True, blank=True)
    bathrooms = models.DecimalField(max_digits=3, decimal_places=1, default=1.0)
    city = models.CharField(max_length=100)  
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)

    property_type = models.CharField(
            max_length=20,
            choices=PROPERTY_TYPES,
            default='residential'  # Default to 'residential' to avoid migration issues
        )

def __str__(self):
    return f"{self.apt_number}, {self.street_address}, {self.is_available}, {self.state} {self.street_address}, {self.city}, {self.state}  ({self.property_type})"