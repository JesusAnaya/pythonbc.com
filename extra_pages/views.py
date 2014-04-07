from django.views.generic import ListView
from .models import TalkPage, CoursePage


class Talks(ListView):
    template_name = "extra_pages/videos.html"
    queryset = TalkPage.objects.published()
    context_object_name = 'posts'
    paginate_by = 10


class Courses(ListView):
    template_name = "extra_pages/videos.html"
    queryset = CoursePage.objects.published()
    context_object_name = 'posts'
    paginate_by = 10
