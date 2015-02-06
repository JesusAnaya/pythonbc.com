from django.conf.urls import patterns, url
from .views import Talks, Courses, Galleries

urlpatterns = patterns("",
    url(r"^charlas-y-talleres/$", Talks.as_view(), name="talks"),
    url(r"^cursos/$", Courses.as_view(), name="courses"),
    url(r"^galerias/$", Galleries.as_view(), name="gallery"),
)
