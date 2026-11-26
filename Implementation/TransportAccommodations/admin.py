from django.contrib import admin
from .models import Transportation, Accommodation


@admin.register(Transportation)
class TransportationAdmin(admin.ModelAdmin):
    list_display = ("route_name", "origin", "destination", "transport_type", "estimated_cost")
    list_filter = ("transport_type",)
    search_fields = ("route_name", "origin", "destination")


@admin.register(Accommodation)
class AccommodationAdmin(admin.ModelAdmin):
    list_display = ("name", "location", "accommodation_type", "price_per_night")
    list_filter = ("accommodation_type",)
    search_fields = ("name", "location", "amenities")
