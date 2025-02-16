from django.urls import path
from .views import maintenance_create

urlpatterns = [
    path("maintenance/new/", maintenance_create, name="maintenance_create"),
]
