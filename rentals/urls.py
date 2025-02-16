from django.urls import path
from . import views  # Import the views from the current app

urlpatterns = [
    path('residential/', views.residential_list, name='residential_list'),
    path('penwell/', views.penwell_list, name='penwell_list'),
    path('penwell/<int:pk>/', views.penwell_detail, name='penwell_detail'),  
    path('residential/<int:pk>/', views.residential_detail, name='residential_detail'),  
]