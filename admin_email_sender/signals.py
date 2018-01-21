from django.conf import settings
from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from admin_email_sender.models import SendEmail
from admin_email_sender.utils import EmailThread, replace_text


@receiver(m2m_changed, sender=SendEmail.users.through)
def send_email_signal(sender, instance, **kwargs):
    users = instance.users.all()
    text = instance.text
    html_text = text.replace('\n', '<br>')
    if instance.template:
        template = instance.template.html.replace('\n', '<br>')
        if '@body' in template:
            html_text = template.replace('@body', instance.text)
        else:
            instance.status = False
            instance.save()
            raise Exception('Error, need @body')
    if users:
        for user in users:
            EmailThread(subject=instance.subject,
                        message=replace_text(text, user),
                        from_email=settings.EMAIL_HOST_USER,
                        recipient_list=[user.email],
                        fail_silently=True,
                        html_message=replace_text(html_text, user)).start()
        instance.status = True

    instance.save()
