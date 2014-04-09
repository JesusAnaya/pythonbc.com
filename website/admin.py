from django.contrib import admin
from mezzanine.generic.models import Keyword

# Add Keyword model to admin panel
class KeywordAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    list_editable = ('slug',)


admin.site.register(Keyword, KeywordAdmin)
