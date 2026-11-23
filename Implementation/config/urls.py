from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("destinations.urls")),
    path("itineraries/", include("itineraries.urls")),
]
