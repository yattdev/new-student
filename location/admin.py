from django.contrib import admin
from .models import Apartment,Amenity,Reservation
# Register your models here.
admin.site.register(Apartment)
admin.site.register(Amenity)
admin.site.register(Reservation)