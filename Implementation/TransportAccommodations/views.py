from django.shortcuts import render
from .models import Transportation, Accommodation


def transport_accommodation_list(request):
    transportations = Transportation.objects.all()
    accommodations = Accommodation.objects.all()
    return render(
        request,
        "TransportAccommodations/overview.html",
        {
            "transportations": transportations,
            "accommodations": accommodations,
        },
    )
