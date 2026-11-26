from django.urls import path
from . import views

app_name = "transport_accommodations"

urlpatterns = [
    path("", views.transport_accommodation_list, name="overview"),
    path("transportation/<int:pk>/", views.transportation_detail, name="transportation_detail"),
    path("accommodation/<int:pk>/", views.accommodation_detail, name="accommodation_detail"),
]
