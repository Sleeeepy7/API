from datetime import datetime

from django.test import TestCase
from .models import Service


class ServiceTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        service_test = Service.objects.create(from_date=datetime.now(), to_date=datetime.now(),
                                              views=100, clicks=100, cost=100)
        service_test.save()

    def test_service_contents(self):
        service = Service.objects.get(id=1)
        from_date = f'{service.from_date}'
        to_date = f'{service.to_date}'
        views = f'{service.views}'
        clicks = f'{service.clicks}'
        cost = f'{service.cost}'
        self.assertEqual(views, '100')
        self.assertEqual(clicks, '100')
        self.assertEqual(cost, '100.00')

