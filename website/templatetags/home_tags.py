from django import template
from django.conf import settings
from mezzanine.blog.models import BlogPost
register = template.Library()


@register.inclusion_tag("blog/home_blog_posts.html")
def render_recent_posts():
    return {
        'blog_posts': BlogPost.objects.published()[:3],
        'MEDIA_URL': settings.MEDIA_URL
    }
