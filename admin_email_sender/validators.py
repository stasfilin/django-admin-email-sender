from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_tags(value):
    if '@body' not in value:
        raise ValidationError(
            _('I can find @body tag'),
            params={'value': value},
        )
