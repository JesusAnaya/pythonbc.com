from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from copy import deepcopy
from .models import TalkPage, BlankPage

page_fieldsets = deepcopy(PageAdmin.fieldsets)
page_fieldsets[0][1]["fields"].insert(-2, "video")
page_fieldsets[0][1]["fields"].insert(-2, "content")


class TalkPageAdmin(PageAdmin):
    fieldsets = page_fieldsets


admin.site.register(TalkPage, TalkPageAdmin)
admin.site.register(BlankPage, PageAdmin)
