from django.conf.urls import patterns, url
from .views import Talks, Courses, Galleries

urlpatterns = patterns("",
    url(r"^talks/$", Talks.as_view(), name="talks"),
    url(r"^courses/$", Courses.as_view(), name="courses"),
    url(r"^galleries/$", Galleries.as_view(), name="galleries"),
)
