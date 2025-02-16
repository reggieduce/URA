
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Contact

def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contact_list.html', {'contacts': contacts})

def contact_detail(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    return render(request, 'contact_detail.html', {'contact': contact})