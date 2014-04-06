from django.contrib.sites.models import Site


def home_settings(request):
    home_url = "http://%s" % Site.objects.get_current()

    return {
        'HOME_URL': home_url,
    }
