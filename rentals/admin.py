from django.contrib import admin

from .models import RentalProperty

@admin.register(RentalProperty)
class RentalPropertyAdmin(admin.ModelAdmin):
    list_display = ('street_address', 'city', 'state')