from django.urls import path
from . import views

app_name = "itineraries"

urlpatterns = [
    path("", views.itinerary_list, name="itinerary_list"),
    path("<int:pk>/", views.itinerary_detail, name="itinerary_detail"),
]
