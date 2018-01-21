import threading

from django.core.mail import EmailMultiAlternatives


class EmailThread(threading.Thread):
    def __init__(self,
                 subject: str,
                 message: str,
                 from_email: str,
                 recipient_list: list,
                 fail_silently: bool,
                 html_message: str):
        self.subject = subject
        self.message = message
        self.recipient_list = recipient_list
        self.from_email = from_email
        self.fail_silently = fail_silently
        self.html_message = html_message
        threading.Thread.__init__(self)

    def run(self):
        msg = EmailMultiAlternatives(subject=self.subject,
                                     body=self.message,
                                     from_email=self.from_email,
                                     to=self.recipient_list)
        msg.attach_alternative(self.html_message, 'text/html')
        msg.send(self.fail_silently)


def replace_text(text, user):
    text = text.replace('@username', user.username)
    text = text.replace('@fullName', user.get_full_name())
    text = text.replace('@firstName', user.first_name)
    text = text.replace('@lastName', user.last_name)

    return text
