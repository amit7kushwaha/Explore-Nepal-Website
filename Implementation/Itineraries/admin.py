from django.contrib import admin
from .models import Itinerary, ItineraryDay


class ItineraryDayInline(admin.TabularInline):
    model = ItineraryDay
    extra = 1


@admin.register(Itinerary)
class ItineraryAdmin(admin.ModelAdmin):
    list_display = ("title", "destination", "duration_days", "difficulty", "is_published")
    list_filter = ("is_published", "difficulty")
    search_fields = ("title", "destination")
    inlines = [ItineraryDayInline]
