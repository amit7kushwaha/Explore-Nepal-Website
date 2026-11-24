"""Admin login/dashboard pages.  SRS: FR-21, FR-23, FR-24, FR-25."""
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.db.models import Count
from django.shortcuts import render

from itineraries.models import Itinerary


@login_required                      # FR-21 / FR-23: anonymous visitors are sent to the login page
def dashboard(request):
    if not request.user.is_staff:    # logged in but NOT an administrator -> 403
        raise PermissionDenied
    counts = {row["status"]: row["n"] for row in Itinerary.objects.values("status").annotate(n=Count("id"))}
    context = {
        "itinerary_counts": [(label, counts.get(value, 0)) for value, label in Itinerary.Status.choices],
    }
    return render(request, "accounts/dashboard.html", context)
