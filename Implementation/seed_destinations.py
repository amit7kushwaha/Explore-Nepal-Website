from django.core.management.base import BaseCommand
from destinations.models import Destination


class Command(BaseCommand):
    help = "Add Nepal tourist destinations"

    def handle(self, *args, **kwargs):
        places = [
            {
                "name": "Pokhara",
                "location": "Kaski, Gandaki Province",
                "description": "Pokhara is famous for Phewa Lake, mountain views, caves and natural beauty.",
                "best_time_to_visit": "September to November and March to May",
                "travel_information": "Reach Pokhara by road or flight from Kathmandu. Local buses and taxis are available.",
                "image_url": ""
            },
            {
                "name": "Chitwan National Park",
                "location": "Chitwan, Bagmati Province",
                "description": "Chitwan is famous for wildlife, forests, birds and biodiversity.",
                "best_time_to_visit": "October to March",
                "travel_information": "Reachable by road from Kathmandu and Pokhara.",
                "image_url": ""
            },
            {
                "name": "Lumbini",
                "location": "Rupandehi, Lumbini Province",
                "description": "Lumbini is the birthplace of Gautama Buddha and an important historical destination.",
                "best_time_to_visit": "October to March",
                "travel_information": "Accessible by road and through Gautam Buddha International Airport.",
                "image_url": ""
            },
            {
                "name": "Kathmandu",
                "location": "Kathmandu, Bagmati Province",
                "description": "Kathmandu is the capital of Nepal, famous for temples and cultural heritage.",
                "best_time_to_visit": "September to November and February to April",
                "travel_information": "Accessible through Tribhuvan International Airport and road networks.",
                "image_url": ""
            },
            {
                "name": "Everest Base Camp",
                "location": "Solukhumbu, Koshi Province",
                "description": "A famous trekking destination with spectacular Himalayan mountain views.",
                "best_time_to_visit": "March to May and September to November",
                "travel_information": "The journey generally involves a flight to Lukla followed by trekking.",
                "image_url": ""
            },
            {
                "name": "Rara Lake",
                "location": "Mugu, Karnali Province",
                "description": "Rara is Nepal's largest lake, surrounded by forests and mountains.",
                "best_time_to_visit": "April to June and September to October",
                "travel_information": "Accessible through flights and road travel followed by local trekking routes.",
                "image_url": ""
            },
            {
                "name": "Bandipur",
                "location": "Tanahun, Gandaki Province",
                "description": "Bandipur is a traditional hilltop town known for architecture and mountain views.",
                "best_time_to_visit": "September to May",
                "travel_information": "Accessible by road from Kathmandu and Pokhara.",
                "image_url": ""
            },
            {
                "name": "Ilam",
                "location": "Ilam, Koshi Province",
                "description": "Ilam is famous for green tea gardens and beautiful hills.",
                "best_time_to_visit": "March to May and October to November",
                "travel_information": "Accessible by road from Birtamod and other eastern cities.",
                "image_url": ""
            },
            {
                "name": "Janakpur",
                "location": "Dhanusha, Madhesh Province",
                "description": "Janakpur is famous for Janaki Temple and Mithila culture.",
                "best_time_to_visit": "October to March",
                "travel_information": "Accessible by road and through Janakpur Airport.",
                "image_url": ""
            },
            {
                "name": "Annapurna Region",
                "location": "Gandaki Province",
                "description": "The Annapurna region is popular for trekking and Himalayan scenery.",
                "best_time_to_visit": "March to May and September to November",
                "travel_information": "Most trekking routes begin from Pokhara. Trekking permits may be required.",
                "image_url": ""
            }
        ]

        for place in places:
            Destination.objects.update_or_create(
                name=place["name"],
                defaults=place
            )

        self.stdout.write(
            self.style.SUCCESS("Nepal destinations added successfully!")
        )