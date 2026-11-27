from django.db import models


class Transportation(models.Model):
    TRANSPORT_TYPES = [
        ("Flight", "Flight"),
        ("Tourist Bus", "Tourist Bus"),
        ("Private Jeep", "Private Jeep"),
        ("Local Bus", "Local Bus"),
    ]

    route_name = models.CharField(max_length=150)
    origin = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    transport_type = models.CharField(max_length=30, choices=TRANSPORT_TYPES, default="Tourist Bus")
    duration = models.CharField(max_length=60, help_text="e.g., 6 hours or 35 mins")
    estimated_cost = models.DecimalField(max_digits=8, decimal_places=2)
    schedule_notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.route_name} ({self.transport_type})"


class Accommodation(models.Model):
    ACCOMMODATION_TYPES = [
        ("Hotel", "Hotel"),
        ("Tea House", "Tea House"),
        ("Resort", "Resort"),
        ("Lodge", "Lodge"),
        ("Homestay", "Homestay"),
    ]

    name = models.CharField(max_length=150)
    location = models.CharField(max_length=120)
    accommodation_type = models.CharField(max_length=30, choices=ACCOMMODATION_TYPES, default="Hotel")
    price_per_night = models.DecimalField(max_digits=8, decimal_places=2)
    amenities = models.TextField(blank=True)
    contact_info = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return f"{self.name} - {self.location}"
