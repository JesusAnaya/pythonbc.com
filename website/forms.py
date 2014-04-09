from django import forms
from django.conf import settings
STATIC_URL = settings.STATIC_URL


class TinyMceWidget(forms.Textarea):
    class Media:
        js = (
            "%stiny_mce/tiny_mce.js" % STATIC_URL,
            "%sjs/tinymce.js" % STATIC_URL,
        )

    def __init__(self, *args, **kwargs):
        super(TinyMceWidget, self).__init__(*args, **kwargs)
        self.attrs["class"] = "mceEditor"
