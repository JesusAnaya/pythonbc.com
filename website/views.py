from django.views.generic import View
from django.http import Http404
from website.feeds import PostsMediaAtom, FeedMediaRSS


class FeedView(View):
    def get(self, request, format, **kwargs):
        """
        Blog posts feeds - maps format to the correct feed view.
        """

        feeds = {
            'rss': FeedMediaRSS,
            'atom': PostsMediaAtom
        }

        try:
            return feeds[format](**kwargs)(request)
        except KeyError:
            raise Http404()
