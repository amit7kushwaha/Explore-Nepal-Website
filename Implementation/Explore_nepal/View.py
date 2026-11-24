"""Public pages for itineraries.  SRS: FR-11, FR-12, FR-13, FR-30."""
from django.views.generic import DetailView, ListView

from .models import Itinerary


class ItineraryListView(ListView):
    """FR-11: list PUBLISHED itineraries only. NFR-03: paginated."""
    model = Itinerary
    template_name = "itineraries/itinerary_list.html"
    context_object_name = "itineraries"
    paginate_by = 9

    def get_queryset(self):
        return Itinerary.objects.published()


