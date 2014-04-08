from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from copy import deepcopy
from .models import Event

admin.site.register(Event, PageAdmin)
