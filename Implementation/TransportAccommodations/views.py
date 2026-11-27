from django.db.models import Q
from django.shortcuts import get_object_or_404, render
from .models import Accommodation, Transportation


def transport_accommodation_list(request):
    query = request.GET.get("q", "").strip()
    transport_type = request.GET.get("transport_type", "")
    accommodation_type = request.GET.get("accommodation_type", "")

    transportations = Transportation.objects.all()
    accommodations = Accommodation.objects.all()

    if query:
        transportations = transportations.filter(
            Q(route_name__icontains=query)
            | Q(origin__icontains=query)
            | Q(destination__icontains=query)
        )
        accommodations = accommodations.filter(
            Q(name__icontains=query)
            | Q(location__icontains=query)
            | Q(amenities__icontains=query)
        )

    if transport_type:
        transportations = transportations.filter(transport_type=transport_type)

    if accommodation_type:
        accommodations = accommodations.filter(accommodation_type=accommodation_type)

    return render(
        request,
        "TransportAccommodations/overview.html",
        {
            "transportations": transportations,
            "accommodations": accommodations,
            "query": query,
            "selected_transport_type": transport_type,
            "selected_accommodation_type": accommodation_type,
            "transport_types": Transportation.TRANSPORT_TYPES,
            "accommodation_types": Accommodation.ACCOMMODATION_TYPES,
        },
    )


def transportation_detail(request, pk):
    transportation = get_object_or_404(Transportation, pk=pk)
    return render(
        request,
        "TransportAccommodations/transportation_detail.html",
        {"transportation": transportation},
    )


def accommodation_detail(request, pk):
    accommodation = get_object_or_404(Accommodation, pk=pk)
    return render(
        request,
        "TransportAccommodations/accommodation_detail.html",
        {"accommodation": accommodation},
    )
