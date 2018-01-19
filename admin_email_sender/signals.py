from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from django.core.mail import send_mass_mail
from django.conf import settings

from .models import SendEmail


@receiver(m2m_changed, sender=SendEmail.users.through)
def send_email_signal(sender, instance, **kwargs):
    users = instance.users.all()
    data = []
    if users:
        for user in users:
            data.append((instance.subject, instance.text, settings.EMAIL_HOST_USER, [user.email]))
    try:
        send_mass_mail(data)
        instance.status = True
    except Exception as e:
        instance.status = False

    instance.save()