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

    def save_model(self, request, obj, form, change):
        # FR-29: remember WHICH admin created / changed the record
        if not change:
            obj.created_by = request.user
        obj.updated_by = request.user
        super().save_model(request, obj, form, change)

    @admin.action(description="Publish selected itineraries")
    def publish_selected(self, request, queryset):
        done = 0
        for obj in queryset:
            missing = obj.missing_for_publish()
            if missing:  # FR-28
                self.message_user(
                    request, f"'{obj.title}' was NOT published. Missing: {', '.join(missing)}.", messages.WARNING
                )
                continue
            obj.status = Itinerary.Status.PUBLISHED
            obj.updated_by = request.user
            obj.save()
            done += 1
        if done:
            self.message_user(request, f"{done} itinerary(ies) published.", messages.SUCCESS)

    @admin.action(description="Unpublish selected itineraries")
    def unpublish_selected(self, request, queryset):
        n = queryset.update(status=Itinerary.Status.UNPUBLISHED, updated_by=request.user)
        self.message_user(request, f"{n} itinerary(ies) unpublished.", messages.SUCCESS)

    @admin.action(description="Archive selected itineraries")
    def archive_selected(self, request, queryset):
        n = queryset.update(status=Itinerary.Status.ARCHIVED, updated_by=request.user)
        self.message_user(request, f"{n} itinerary(ies) archived.", messages.SUCCESS)
