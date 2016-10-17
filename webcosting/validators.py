from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

def validate_lower_than_100(value):
    if value > 100:
        raise ValidationError(
            _('%(value)s must be lower than 100'),
            params={'value': value},
        )