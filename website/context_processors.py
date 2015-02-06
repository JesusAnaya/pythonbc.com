from django.contrib.sites.models import Site
from mezzanine.conf import settings

def base_settings(request):
    home_url = "https://%s" % Site.objects.get_current()

    return {
        'HOME_URL': home_url,
        'FOOTER_MESSAGE': settings.FOOTER_MESSAGE
    }
