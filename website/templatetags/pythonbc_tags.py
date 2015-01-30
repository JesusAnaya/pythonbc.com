from django import template
from django.conf import settings
register = template.Library()


@register.simple_tag
def short_url_by_googl(url):
    return url
