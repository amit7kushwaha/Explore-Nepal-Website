from django.urls import path
from . import views

app_name = "transport_accommodations"

urlpatterns = [
    path("", views.transport_accommodation_list, name="overview"),
]
