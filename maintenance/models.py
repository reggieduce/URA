from django.db import models

class Maintenance(models.Model):

    URGENCY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    ]

    urgency = models.CharField(max_length=10, choices=URGENCY_CHOICES, default='Medium')
    street_address = models.CharField(max_length=200)
    description = models.TextField()
    date_reported = models.DateTimeField(auto_now_add=True)
    pending = models.BooleanField(default=True)


    def __str__(self):
        return f"{self.urgency} - {self.street_address} ({self.date_reported.strftime('%Y-%m-%d')})"
