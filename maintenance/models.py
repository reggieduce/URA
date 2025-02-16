from django.db import models

class Maintenance(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_reported = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title