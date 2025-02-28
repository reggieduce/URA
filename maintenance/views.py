from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

# Create your views here.
from .models import Maintenance

def maintenance_list(request):
    if request.method == "POST":
        urgency = request.POST.get("urgency", "Medium")
        street_address = request.POST.get("street_address")
        description = request.POST.get("description")
        Maintenance.objects.create(urgency = urgency, street_address = street_address,description=description)
        return redirect("maintenance_list")  # Reload the page to show new entries
    
    maintenances = Maintenance.objects.all()
    return render(request, 'maintenance_list.html', {'maintenances': maintenances})



def home_view(request):
    maintenancehome =  Maintenance.objects.filter(urgency="High").order_by('-date_reported')
    return render(request, 'home.html', {'maintenancehome': maintenancehome})

def maintenance_detail(request, pk):
    maintenance = get_object_or_404(Maintenance, pk=pk)
    return render(request, 'maintenance_detail.html', {'maintenance': maintenance})

def maintenance_edit(request, pk):
    maintenance = get_object_or_404(Maintenance, pk=pk)
    
    if request.method == "POST":
        # Update fields based on POST data
        maintenance.urgency = request.POST.get("urgency", maintenance.urgency)
        maintenance.street_address = request.POST.get("street_address", maintenance.street_address)
        maintenance.description = request.POST.get("description", maintenance.description)
        maintenance.save()
        # Redirect to the detail view after updating
        return redirect(reverse('maintenance_detail', args=[maintenance.pk]))
    
    # If it's a GET request, just render the form with current data
    context = {
        'maintenance': maintenance
    }
    return render(request, 'maintenance_edit.html', context)