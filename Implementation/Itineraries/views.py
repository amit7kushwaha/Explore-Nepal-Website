from django.shortcuts import get_object_or_404, render
from .models import Itinerary

def itinerary_list(request):
    itineraries = Itinerary.objects.filter(is_published=True)
    return render(request, "Itineraries/itinerary_list.html", {"itineraries": itineraries})

def itinerary_detail(request, pk):
    itinerary = get_object_or_404(Itinerary, pk=pk, is_published=True)
    return render(request, "Itineraries/itinerary_detail.html", {"itinerary": itinerary})
