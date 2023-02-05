from django.shortcuts import get_object_or_404,render

# Create your views here.
from .models import Country,Destination,DestinationDetail

def product_all(request):
    destination = Destination.objects.all()         #new
    country = Country.objects.all()
    return render(request, 'travel_blog/home.html',{'destinations' : destination,'country' : country})

def about(request):
    country = Country.objects.all()
    destination = Destination.objects.all() 
    return render(request,'travel_blog/about.html',{'country':country,'destinations' : destination})

def discover(request):
    country = Country.objects.all()
    destination = Destination.objects.all() 
    return render(request,'travel_blog/discover.html',{'country':country,'destinations' : destination})