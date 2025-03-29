from django.contrib.auth import get_user_model
from django.test import TestCase

from kitchen_service.models import DishType


class ModelTests(TestCase):
    def test_dish_type_str(self):
        dish_type = DishType.objects.create(
            name="Test_name",
        )
        self.assertEqual(str(dish_type),
                         f"{dish_type.name}")

    def test_cook_str(self):
        cook = get_user_model().objects.create(
            username="test",
            password="test123",
            years_of_experience="10",
            first_name="test_first",
            last_name="test_last",
        )
        self.assertEqual(str(cook),
                         f"{cook.username}"
                         f" ({cook.first_name}"
                         f" {cook.last_name})")

    def test_create_cook_with_years_of_experience(self):
        username = "test"
        password = "test123"
        years_of_experience = "10"
        cook = get_user_model().objects.create_user(
            username=username,
            password=password,
            years_of_experience=years_of_experience,
        )
        self.assertEqual(cook.username, username)
        self.assertEqual(cook.years_of_experience, years_of_experience)
        self.assertEqual(cook.check_password(password), True)
