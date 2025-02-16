from django.shortcuts import render

# Create your views here.

def home_page_view(request): # new
    return render(request, "home.html")

class AboutPageView(TemplateView): # new
    template_name = "penwellabout.html"

class AboutPageView(TemplateView): # new
    template_name = "residentialbout.html"