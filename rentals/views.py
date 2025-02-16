from django.shortcuts import render, get_object_or_404

from .models import RentalProperty


# Create your views here.

def residential_list(request):
    residential_properties = RentalProperty.objects.filter(property_type='residential')
    return render(request, 'residentialrentals.html', {'residentialproperties': residential_properties})

def penwell_list(request):
    penwell_properties = RentalProperty.objects.filter(property_type__in=['penwell', 'commercial', 'airbnb', 'Penwell', 'Commercial', 'Airbnb'])
    return render(request, 'penwellrentals.html', {'penwellproperties': penwell_properties})

def penwell_detail(request, pk):
    penwell_detail = get_object_or_404(RentalProperty, pk=pk)
    return render(request, 'penwelldetail.html', {'penwelldetail': penwell_detail})

def residential_detail(request, pk):
    residential_detail = get_object_or_404(RentalProperty, pk=pk)
    return render(request, 'residentialdetail.html', {'residentialdetail': residential_detail})