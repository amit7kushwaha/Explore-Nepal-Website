from django.db import models

class Destination(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.TextField()
    best_time_to_visit = models.CharField(max_length=100)
    travel_information = models.TextField()
    image_url = models.URLField(blank=True)

    def __str__(self):
        return self.name