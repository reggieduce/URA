from django.urls import path
from . import views

# Create your views here.
urlpatterns = [
    path('', views.contact_list, name='contact_list'),
    path('<int:pk>/', views.contact_detail, name='contact_detail'),
]