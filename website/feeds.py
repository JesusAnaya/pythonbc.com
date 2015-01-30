from __future__ import unicode_literals

from django.conf import settings
from django.utils.feedgenerator import Rss201rev2Feed, Atom1Feed
from mezzanine.blog.feeds import PostsRSS, PostsAtom


class MediaRssFeed(Rss201rev2Feed):

    def rss_attributes(self):
        attrs = super(MediaRssFeed, self).rss_attributes()
        attrs['xmlns:dc'] = "http://purl.org/dc/elements/1.1/"
        attrs['xmlns:media'] = 'http://search.yahoo.com/mrss/'
        return attrs

    def add_item_elements(self, handler, item):
        """
        Callback to add thumbnail element to each item (item/entry) element.
        """
        super(MediaRssFeed, self).add_item_elements(handler, item)
        thumbnail = {
            'url': item['thumbnail_url']
        }
        
        if 'thumbnail_width' in item:
            thumbnail['width'] = str(item['thumbnail_width'])

        if 'thumbnail_height' in item:
            thumbnail['height'] = str(item['thumbnail_height'])

        handler.addQuickElement(u"media:thumbnail", '', thumbnail)


class FeedMediaRSS(PostsRSS):
    ''' Sanico RSS Cunstom blog with image'''
    feed_type = MediaRssFeed

    def get_image_url(self, item):
        return '{0}{1}'.format(settings.MEDIA_URL, item.featured_image)

    def item_extra_kwargs(self, article):
        """
        Return a dictionary to the feedgenerator for each item to be added to the feed.
        If the object is a Gallery, uses a random sample image for use as the feed Item
        """

        item = {
            'thumbnail_url': self.get_image_url(article),
            # Optional
            'thumbnail_width': 750,
            'thumbnail_height': 400,
        }
        return item


class Atom1FeedWithMedia(MediaRssFeed, Atom1Feed):
    pass


class PostsMediaAtom(PostsAtom):
    """
    Atom feed for all blog posts.
    """

    feed_type = Atom1FeedWithMedia

    def subtitle(self):
        return self.description()
