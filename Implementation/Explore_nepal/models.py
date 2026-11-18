"""Itinerary / travel-guide model.  SRS: FR-11, FR-12, FR-13, FR-27, FR-28, FR-29, FR-30, BR-01."""
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse


class ItineraryQuerySet(models.QuerySet):
    def published(self):
        """Only published itineraries may be shown to visitors (FR-30, BR-01)."""
        return self.filter(status=Itinerary.Status.PUBLISHED)


class Itinerary(models.Model):
    class Status(models.TextChoices):
        DRAFT = "draft", "Draft"
        PUBLISHED = "published", "Published"
        UNPUBLISHED = "unpublished", "Unpublished"
        ARCHIVED = "archived", "Archived"

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=220, unique=True, help_text="Used in the web address, e.g. 'annapurna-circuit-10-days'.")
    duration_days = models.PositiveSmallIntegerField(null=True, blank=True, help_text="Number of days.")
    summary = models.CharField(max_length=300, blank=True, help_text="One or two sentences shown on the list page.")
    route_stops = models.TextField(blank=True, help_text="Write ONE stop per line, in order. Example: Kathmandu")
    description = models.TextField(blank=True)
    practical_notes = models.TextField(blank=True, help_text="Permits, best season, difficulty, etc.")
    destinations = models.ManyToManyField(
        "destinations.Destination", blank=True, related_name="itineraries",
        help_text="Destinations that are part of this itinerary.",
    )
    status = models.CharField(max_length=12, choices=Status.choices, default=Status.DRAFT)

    # FR-29: timestamps + responsible administrator
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL,
        related_name="itineraries_created", editable=False,
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.SET_NULL,
        related_name="itineraries_updated", editable=False,
    )

    objects = ItineraryQuerySet.as_manager()

    class Meta:
        ordering = ["title"]
        verbose_name = "itinerary"
        verbose_name_plural = "itineraries"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("itineraries:detail", kwargs={"slug": self.slug})

    @property
    def stops_list(self):
        """route_stops text -> clean list (one stop per line)."""
        return [line.strip() for line in self.route_stops.splitlines() if line.strip()]

    def missing_for_publish(self):
        """Names of required fields that are still empty (FR-28)."""
        missing = []
        if not self.duration_days:
            missing.append("duration_days")
        if not self.stops_list:
            missing.append("route_stops")
        if not self.description.strip():
            missing.append("description")
        return missing

    def clean(self):
        # FR-28: required content must be filled in BEFORE an itinerary can be published
        if self.status == self.Status.PUBLISHED:
            missing = self.missing_for_publish()
            if missing:
                raise ValidationError(
                    {name: "This field is required before the itinerary can be published." for name in missing}
                )

    def published_destinations(self):
        """Related destinations visitors may see (FR-05, FR-30).
        ASSUMES Kalpana's Destination has a `status` field with the value 'published'."""
        return self.destinations.filter(status="published")
