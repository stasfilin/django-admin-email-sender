from django.contrib.auth.models import User
from django.db import models


class SendEmail(models.Model):
    subject = models.CharField(max_length=100, null=False, blank=False)
    text = models.TextField(null=False, blank=False)
    users = models.ManyToManyField(User, blank=False, related_name='+')
    status = models.BooleanField(default=False)

    created_at = models.DateTimeField(
        auto_now_add=True,
        null=True
    )
