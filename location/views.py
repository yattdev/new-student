from django.shortcuts import render,redirect,get_object_or_404
from .models import Apartment,Reservation
from accounts.models import Agent
# Create your views here.

def index(request):
    context={
        'apartments': Apartment.objects.all(),
        'agents': Agent.objects.all(),
        'posts': Reservation.objects.filter(apartment__is_available=False) # reservation --> non dispo donc all() aussi passe
    }
    return render(request,'location/index.html',context=context)
def detail(request,slug):
    apartment=get_object_or_404(Apartment,slug=slug)
    return render(request,'location/detail.html',context={'apartment':apartment})
def about(request):
    return render(request,'location/about.html',context={'agents':Agent.objects.all()})

def blog(request,variable):
    if variable == 'grid':
        apartments=Apartment.objects.filter(is_available=False)
        posts=Reservation.objects.filter(apartment=apartments)
        return render(request,f"location/blog-grid.html",context={'posts',posts})
    else:
        apartment = Apartment.objects.get(is_available=False,slug=variable)
        post = Reservation.objects.get(apartment=apartment)
        return render(request,f"location/blog-single.html",context={'post',post})

def property(request,variable):
    if variable=='grid':
        return render(request,f'location/property-grid.html',context={'apartments':Apartment.objects.all()})
    else:
        apartment=get_object_or_404(Apartment,slug=variable)
        return render(request,f'location/property-single.html',context={'apartment':apartment})
def contact(request):
    return render(request,'location/contact.html')
