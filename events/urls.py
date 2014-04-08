from django.conf.urls import patterns, url
from .views import Events, EventDetail

urlpatterns = patterns("",
    url(r"^$", Events.as_view(), name="events"),
    url(r"^(?P<slug>.*)/$", EventDetail.as_view(), name="event"),
)
