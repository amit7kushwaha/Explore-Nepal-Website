"""Admin screens for itineraries.  SRS: FR-27, FR-28, FR-29."""
from django.contrib import admin, messages

from .models import Itinerary


@admin.register(Itinerary)
class ItineraryAdmin(admin.ModelAdmin):
    list_display = ("title", "duration_days", "status", "updated_at", "updated_by")
    list_filter = ("status",)
    search_fields = ("title", "summary", "description")
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ("destinations",)
    readonly_fields = ("created_at", "updated_at", "created_by", "updated_by")
    actions = ["publish_selected", "unpublish_selected", "archive_selected"]

   
