from django.contrib.auth.models import User
from django.core import mail
from django.test import TestCase

from admin_email_sender.models import SendEmail


class SendEmailTest(TestCase):

    def test_create_send_email_model_without_users(self):
        send = SendEmail()
        send.subject = 'Test Subject'
        send.text = 'Test Text'
        send.save()

        assert SendEmail.objects.count() is 1
        assert len(mail.outbox) is 0

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
        assert len(mail.outbox) is 10
