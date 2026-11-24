from django.urls import path

from . import views

app_name = "itineraries"

urlpatterns = [
    path("", views.ItineraryListView.as_view(), name="list"),
    path("<slug:slug>/", views.ItineraryDetailView.as_view(), name="detail"),
]
