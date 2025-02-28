from django.urls import path
from . import views

# Create your views here.
urlpatterns = [
    path('', views.home_view, name='home'),
    path('maintenance/', views.maintenance_list, name='maintenance_list'),
    path('<int:pk>/', views.maintenance_detail, name='maintenance_detail'),
    path('maintenance/<int:pk>/edit/', views.maintenance_edit, name='maintenance_edit'),
]