from django.test import TestCase
from django.urls import reverse

DRIVER_URL = reverse("kitchen_service:cook-list")


class PublicCookTest(TestCase):
    def test_login_required(self):
        res = self.client.get(DRIVER_URL)
        self.assertNotEqual(res.status_code, 200)
