from django import template
from events.models import Event
register = template.Library()


@register.inclusion_tag("events/home.html")
def render_home_events():
    return {'events': Event.objects.published()[:2]}


@register.inclusion_tag("events/notice-bar.html")
def render_home_notice_bar():
    return {'event': Event.objects.published().first()}
