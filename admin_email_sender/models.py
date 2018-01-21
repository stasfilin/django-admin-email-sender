from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

from admin_email_sender.helpers import *
from admin_email_sender.validators import *


class SendEmail(models.Model):
    template = models.ForeignKey('Template', null=True, blank=True, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100, null=False, blank=False)
    text = models.TextField(null=False, blank=False, help_text=BODY_HELPER)
    users = models.ManyToManyField(User, blank=False, related_name='+')
    status = models.BooleanField(default=False)

    created_at = models.DateTimeField(
        auto_now_add=True,
        null=True
    )


class Template(models.Model):
    name = models.CharField(max_length=50, verbose_name=_('Template Name'),
                            null=False, blank=False, help_text=TEMPLATE_NAME)

    html = models.TextField(null=False, default=DEFAULT_HTML,
                            blank=False, verbose_name=_('HTML'), validators=[validate_tags],
                            help_text=TEMPLATE_HTML)

    created_at = models.DateTimeField(
        auto_now_add=True,
        null=True
    )

    def __str__(self):
        return self.name
