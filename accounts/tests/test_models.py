from django.test import TestCase
from django.db.models.signals import pre_delete
from accounts.models import User
from mock import patch
from .factories import UserFactory


class CustomUserTestCase(TestCase):        

    def test_create_custom_user(self):
        user = UserFactory.build()
        user.save()

        self.assertIsNotNone(user.id)
        self.assertEquals(str(user.photo), 'accounts/photos/image.png')
        self.assertEquals(user.biography, "Ola ke ase")
        self.assertEquals(user.google_plus, "http://plus.google.com/test")
        user.delete()

    def test_user_pre_delete(self):
        with patch('accounts.models.user_pre_delete', autospec=True) as mocked_handler:
            pre_delete.connect(mocked_handler, sender=User, dispatch_uid='test_cache_mocked_handler')
            user = UserFactory.create()
            user.delete()
            self.assertEquals(mocked_handler.call_count, 1)
