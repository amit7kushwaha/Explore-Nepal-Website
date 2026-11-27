from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("itineraries/", include("Itineraries.urls")),
    path("transport-accommodations/", include("TransportAccommodations.urls")),
]
