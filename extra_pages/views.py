from django.views.generic import ListView
from .models import TalkPage, CoursePage


class Talks(ListView):
    template_name = "pages/videos.html"
    queryset = TalkPage.objects.published()
    context_object_name = 'posts'


class Courses(ListView):
    template_name = "pages/videos.html"
    queryset = CoursePage.objects.published()
    context_object_name = 'posts'
