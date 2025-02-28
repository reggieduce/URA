
from django.contrib import admin

from .models import Maintenance

@admin.register(Maintenance)
class MaintenanceAdmin(admin.ModelAdmin):
    list_display = ('urgency', 'street_address', 'description', 'date_reported', 'pending')



  