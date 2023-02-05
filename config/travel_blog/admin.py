from django.contrib import admin
from .models import Country,Destination,DestinationDetail
# Register your models here.


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['title','population','space','cities']

@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ['name','slug','country']
    prepopulated_fields ={'slug':('name',)}