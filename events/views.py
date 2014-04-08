from django.views.generic import ListView, DetailView
from .models import Event


class Events(ListView):
    template_name = "events/list.html"
    queryset = Event.objects.published()
    context_object_name = "events"
    pagate_by = 10


class EventDetail(DetailView):
    template_name = "events/detail.html"
    model = Event
    context_object_name = "event"
