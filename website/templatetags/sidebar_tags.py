from django import template
from django.conf import settings
from django.db.models import Count
from mezzanine.blog.models import BlogPost, BlogCategory
register = template.Library()


@register.inclusion_tag("blog/home_blog_posts.html")
def render_recent_posts():
    return {
        'blog_posts': BlogPost.objects.published()[:2],
        'MEDIA_URL': settings.MEDIA_URL
    }


@register.inclusion_tag("sidebars/generic.html")
def render_generic_sidebar():
    return {
        'blog_posts': BlogPost.objects.published()[:3],
        'MEDIA_URL': settings.MEDIA_URL
    }


@register.inclusion_tag("sidebars/blog.html")
def render_blog_sidebar():
    posts = BlogPost.objects.published()
    categories = BlogCategory.objects.filter(blogposts__in=posts)
    categories = list(categories.annotate(post_count=Count("blogposts")))
    return {'categories': categories}
