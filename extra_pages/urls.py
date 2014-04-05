from django.conf.urls import patterns, url
from .views import Talks, Courses

urlpatterns = patterns("",
    url(r"^talks/$", Talks.as_view(), name="talks"),
    url(r"^courses/$", Courses.as_view(), name="courses"),
)
