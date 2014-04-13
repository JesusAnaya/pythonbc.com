from django import template
from django.conf import settings
from mezzanine.galleries.models import GalleryImage
from mezzanine.core.templatetags.mezzanine_tags import thumbnail
from extra_pages.models import TalkPage
register = template.Library()
MEDIA_URL = settings.MEDIA_URL


@register.inclusion_tag("extra_pages/recent_talks.html")
def render_recent_talks():
    talks = TalkPage.objects.published().order_by('-publish_date')
    return {'talks': talks[:5]}


@register.simple_tag
def gallery_get_front_image(page):
    image = GalleryImage.objects.filter(gallery=page).first()
    print "Estae s: image", image.file
    image_url = "%s%s" % (MEDIA_URL, thumbnail(image.file, 230, 157))
    return image_url
