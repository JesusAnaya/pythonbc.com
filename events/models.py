from django.db import models
from django.core.urlresolvers import reverse
from mezzanine.pages.models import Page
from mezzanine.core.models import RichText


class Event(Page, RichText):
    start = models.DateTimeField()
    end = models.DateTimeField()
    where = models.CharField(max_length=255)
    gmap = models.TextField()

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"

    def get_absolute_url(self):
        return reverse('event', kwargs={'slug': self.slug})

    def overridden(self):
        return False