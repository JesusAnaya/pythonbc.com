from django.test import TestCase
from django.contrib.admin.sites import AdminSite
from accounts.admin import CustomUserAdmin
from accounts.models import User
from .factories import UserFactory


class CustomUserAdminTest(TestCase):

    def test_get_image(self):
        spect = "<img src='/media/accounts/photos/image.png' height='60'>"
        user = UserFactory.create()

        user_admin = CustomUserAdmin(User, AdminSite())
        self.assertTrue(user_admin.image(user), spect)
        user.delete()
