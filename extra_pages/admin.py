from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from mezzanine.core.admin import StackedDynamicInlineAdmin
from copy import deepcopy
from .models import TalkPage, BlankPage, CoursePage, Course

talk_fieldsets = deepcopy(PageAdmin.fieldsets)
talk_fieldsets[0][1]["fields"].insert(-2, "video")
talk_fieldsets[0][1]["fields"].insert(-2, "content")


course_fieldsets = deepcopy(PageAdmin.fieldsets)
course_fieldsets[0][1]["fields"].insert(-2, "image")
course_fieldsets[0][1]["fields"].insert(-2, "content")


class CourseInline(StackedDynamicInlineAdmin):
    model = Course


class TalkPageAdmin(PageAdmin):
    fieldsets = talk_fieldsets


class CoursePageAdmin(PageAdmin):
    fieldsets = course_fieldsets
    inlines = (CourseInline,)


admin.site.register(TalkPage, TalkPageAdmin)
admin.site.register(CoursePage, CoursePageAdmin)
admin.site.register(BlankPage, PageAdmin)
