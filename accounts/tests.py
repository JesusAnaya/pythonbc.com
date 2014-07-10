from django.test import TestCase
from .models import User
import factory


class UserFactory(factory.DjangoModelFactory):
    username = "anaya"
    password = factory.PostGenerationMethodCall('set_password', '1234')
    photo = factory.django.ImageField()    
    biography = ""
    google_plus = ""

    class Meta:
        model = User


class UserTest(TestCase):
    def test_create_custom_user(self):
        self.assertIsNotNone(UserFactory().id)
