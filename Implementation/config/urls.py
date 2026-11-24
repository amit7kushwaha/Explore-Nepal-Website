from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),          # Amit
    path("itineraries/", include("itineraries.urls")),    # Amit
    # path("destinations/", include("destinations.urls")),   # Kalpana
    # path("inquiries/", include("inquiries.urls")),         # Sujina
    # path("", include("pages.urls")),                       # Pabitra
]
