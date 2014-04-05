from django.test import TestCase
from datetime import datetime
from .models import TalkPage, BlankPage
import factory


class TalkPageFactory(factory.django.DjangoModelFactory):
    FACTORY_FOR = TalkPage

    title = "Test Title"
    status = 2
    publish_date = datetime.now()
    content = "Content 123..."


class ExtraPagesTest(TestCase):
    def test_create_talk_page(self):
        page = TalkPageFactory(
            video = "https://www.youtube.com/watch?v=2orZu537gWA"
        )
        self.assertTrue(page.id is not None)

    def test_validate_video_field(self):
        page = TalkPageFactory()
        print "Video", page.video
        self.assertFalse(page.id is not None)
