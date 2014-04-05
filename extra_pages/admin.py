from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from mezzanine.pages.models import Page, RichTextPage
from mezzanine.core.admin import StackedDynamicInlineAdmin
from copy import deepcopy
from .models import TalkPage, BlankPage, CoursePage, Course

page_fieldsets = deepcopy(PageAdmin.fieldsets)
page_fieldsets[0][1]["fields"].insert(-1, "use_right_panel")

talk_fieldsets = deepcopy(page_fieldsets)
talk_fieldsets[0][1]["fields"].insert(-2, "video")
talk_fieldsets[0][1]["fields"].insert(-2, "content")

richtext_fieldsets = deepcopy(page_fieldsets)
richtext_fieldsets[0][1]["fields"].insert(4, "content")

course_fieldsets = deepcopy(page_fieldsets)
course_fieldsets[0][1]["fields"].insert(-2, "image")
course_fieldsets[0][1]["fields"].insert(-2, "content")


class ExtraPageAdmin(PageAdmin):
    fieldsets = page_fieldsets


class TalkPageAdmin(PageAdmin):
    fieldsets = talk_fieldsets


class RichTextPageAdmin(PageAdmin):
    fieldsets = richtext_fieldsets


class CourseInline(StackedDynamicInlineAdmin):
    model = Course


class CoursePageAdmin(PageAdmin):
    fieldsets = course_fieldsets
    inlines = (CourseInline,)


admin.site.unregister(Page)
admin.site.unregister(RichTextPage)
admin.site.register(Page, ExtraPageAdmin)
admin.site.register(RichTextPage, RichTextPageAdmin)
admin.site.register(TalkPage, TalkPageAdmin)
admin.site.register(CoursePage, CoursePageAdmin)
admin.site.register(BlankPage, ExtraPageAdmin)
