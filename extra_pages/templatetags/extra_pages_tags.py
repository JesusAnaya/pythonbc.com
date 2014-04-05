from django import template
from extra_pages.models import TalkPage
register = template.Library()


@register.inclusion_tag("extra_pages/recent_talks.html")
def render_recent_talks():
    talks = TalkPage.objects.published()[:4]
    return {'talks': talks}
