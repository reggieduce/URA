from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Bill

def bill_list(request):
    bills = Bill.objects.all()
    return render(request, 'bill_list.html', {'bills': bills})

def bill_detail(request, pk):
    bill = get_object_or_404(Bill, pk=pk)
    return render(request, 'bill_detail.html', {'bill': bill})