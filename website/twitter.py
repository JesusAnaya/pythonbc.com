from twython import Twython
from mezzanine.conf import settings


def public_on_twitter(message):
    settings.use_editable()

    twitter = Twython(
        settings.TWITTER_APP_KEY,
        settings.TWITTER_APP_SECRET,
        settings.TWITTER_ACCESS_TOKEN_KEY,
        settings.TWITTER_ACCESS_TOKEN_SECRET
    )

    twitter.update_status(status=message)
