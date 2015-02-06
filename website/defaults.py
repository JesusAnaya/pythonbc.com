from mezzanine.conf import register_setting

register_setting(
    name="FOOTER_MESSAGE",
    description="The message shown in the page footer.",
    editable=True,
    default="",
)
