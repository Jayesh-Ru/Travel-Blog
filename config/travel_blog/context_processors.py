from .models import Country,Destination

def product_all(request):
    return {
        'destinations' :Destination.objects.all() 
    }

def about(request):
    return{
        'about':Country.objects.all()
    }