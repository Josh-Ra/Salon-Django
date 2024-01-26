from django.contrib import admin
from .models import stylist, Bookings, services
# Register your models here.

class StylstAdmin(admin.ModelAdmin):
    list_display = ("name","description",'image')

admin.site.register(stylist)

class BookingAdmin(admin.ModelAdmin):
    list_display = ["date","time","service"]

admin.site.register(Bookings)

class ServiceAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "image", "description"]

admin.site.register(services)