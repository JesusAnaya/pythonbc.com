from mezzanine.pages.models import Page
from mezzanine.core.models import RichText
from embed_video.fields import EmbedVideoField


class TalkPage(Page, RichText):
    video = EmbedVideoField()

    class Meta:
        verbose_name = "Talk Page"
        verbose_name_plural = "Talk Pages"


class BlankPage(Page):
    class Meta:
        verbose_name = "Blank Page"
        verbose_name_plural = "Blank Pages"
