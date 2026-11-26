from django.test import TestCase
from django.urls import reverse
from .models import Accommodation, Transportation


class TransportAccommodationsTests(TestCase):
    def setUp(self):
        self.flight = Transportation.objects.create(
            route_name="Kathmandu to Pokhara Flight",
            origin="Kathmandu",
            destination="Pokhara",
            transport_type="Flight",
            duration="25 mins",
            estimated_cost="115.00",
        )
        self.hotel = Accommodation.objects.create(
            name="Phewa Lakeside Hotel",
            location="Pokhara",
            accommodation_type="Hotel",
            price_per_night="65.00",
        )

    def test_overview_and_filters(self):
        url = reverse("transport_accommodations:overview")
        self.assertEqual(self.client.get(url).status_code, 200)
        res = self.client.get(url, {"q": "Pokhara", "transport_type": "Flight"})
        self.assertContains(res, "Kathmandu to Pokhara Flight")

    def test_detail_pages(self):
        t_url = reverse("transport_accommodations:transportation_detail", args=[self.flight.pk])
        a_url = reverse("transport_accommodations:accommodation_detail", args=[self.hotel.pk])
        self.assertEqual(self.client.get(t_url).status_code, 200)
        self.assertEqual(self.client.get(a_url).status_code, 200)
