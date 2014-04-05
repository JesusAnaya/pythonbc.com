from django.db import models
from mezzanine.pages.models import Page
from mezzanine.core.models import RichText
from mezzanine.core.fields import FileField
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


class CoursePage(Page, RichText):
    image = FileField(upload_to="courses/", format="Image",
                                max_length=255, null=True)

    class Meta:
        verbose_name = "Course Page"
        verbose_name_plural = "Course Pages"


class Course(models.Model):
    page = models.ForeignKey(CoursePage)
    title = models.CharField(max_length=255)
    video = EmbedVideoField()
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
