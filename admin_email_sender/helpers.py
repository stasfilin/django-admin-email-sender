from django.utils.translation import gettext_lazy as _

TEMPLATE_HTML = _('You can use tags: <br>@body - <b>required</b><br>@username, @fullName, @firstName, @lastName')
TEMPLATE_NAME = _('Template Name')

DEFAULT_HTML = """
<body>
    @body
</body>
"""


BODY_HELPER = _('You can use tags:<br>@username<br>@fullName<br>@firstName<br>@lastName')
