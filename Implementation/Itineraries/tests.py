from django.test import TestCase
from django.urls import reverse
from .models import Itinerary, ItineraryDay


class ItinerariesTests(TestCase):
    def setUp(self):
        self.published = Itinerary.objects.create(
            title="Annapurna Base Camp Trek",
            destination="Pokhara / Annapurna",
            duration_days=7,
            difficulty="Moderate",
            summary="Classic Himalayan trek through Gurung villages.",
            is_published=True,
        )
        ItineraryDay.objects.create(
            itinerary=self.published,
            day_number=1,
            heading="Pokhara to Ulleri",
            description="Drive to Nayapul and trek to Ulleri.",
            overnight_stay="Ulleri Teahouse",
        )
        self.draft = Itinerary.objects.create(
            title="Hidden Draft Route",
            destination="Mustang",
            duration_days=5,
            is_published=False,
        )

    def test_published_list_and_navigation(self):
        list_url = reverse("itineraries:itinerary_list")
        detail_url = reverse("itineraries:itinerary_detail", args=[self.published.pk])

        res = self.client.get(list_url)
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, "Annapurna Base Camp Trek")
        self.assertContains(res, detail_url)
        self.assertContains(res, "informational purposes only")
        self.assertNotContains(res, "Hidden Draft Route")

    def test_detail_and_unpublished_404(self):
        detail_url = reverse("itineraries:itinerary_detail", args=[self.published.pk])
        res = self.client.get(detail_url)
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, "Day 1: Pokhara to Ulleri")
        self.assertContains(res, reverse("itineraries:itinerary_list"))

        draft_url = reverse("itineraries:itinerary_detail", args=[self.draft.pk])
        self.assertEqual(self.client.get(draft_url).status_code, 404)
