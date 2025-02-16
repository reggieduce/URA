from django.urls import path

from .views import home_page_view, AboutPageView, property_list # new

urlpatterns = [
    path("penwellabout/", views.penwell_about, name='penwell_about')),
    path("residentialabout/", AboutPageView.as_view()), # new
    path("", home_page_view),
]

