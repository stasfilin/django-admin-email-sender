from django.contrib.auth.models import User
from django.core import mail
from django.test import TestCase
from django.test import override_settings

from admin_email_sender.models import SendEmail, Template
from admin_email_sender.helpers import DEFAULT_HTML


class SendEmailTest(TestCase):

    def test_create_send_email_model_without_users(self):
        send = SendEmail()
        send.subject = 'Test Subject'
        send.text = 'Test Text'
        send.save()

        assert SendEmail.objects.count() is 1
        assert len(mail.outbox) is 0

    @override_settings(EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend')
    def test_create_send_email_model_with_users(self):
        users = [User.objects.create_user('test_' + str(x),
                                          'test_1' + str(x) + '@test.email',
                                          'password123' + str(x)) for x in range(10)]
        send = SendEmail()
        send.subject = 'Test Subject'
        send.text = 'Test Text'
        send.save()
        send.users.set(users)

        assert send.users.count() is 10


class TemplateTest(TestCase):

    def test_create_template_with_default_data(self):

        template = Template()
        template.name = 'Test'
        template.save()

        assert Template.objects.count() is 1
        assert Template.objects.get(name='Test').html == DEFAULT_HTML
