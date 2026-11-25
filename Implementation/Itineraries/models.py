from django.db import models


class Itinerary(models.Model):
    title = models.CharField(max_length=200)
    destination = models.CharField(max_length=150)
    duration_days = models.PositiveIntegerField(default=1)
    difficulty = models.CharField(max_length=50, default="Moderate")
    summary = models.TextField(blank=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class ItineraryDay(models.Model):
    itinerary = models.ForeignKey(Itinerary, related_name="days", on_delete=models.CASCADE)
    day_number = models.PositiveIntegerField()
    heading = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    overnight_stay = models.CharField(max_length=150, blank=True)

    class Meta:
        ordering = ["day_number"]

    def __str__(self):
        return f"Day {self.day_number}: {self.heading}"
