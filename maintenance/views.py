from django.shortcuts import render, redirect
from .models import Maintenance

def maintenance_create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        Maintenance.objects.create(title=title, description=description)  # Save to database
        return redirect("maintenance_list")  # Redirect to the list page after submitting
    
    return render(request, "maintenance_form.html")  # Show the form page
