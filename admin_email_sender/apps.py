from django.apps import AppConfig


class AdminEmailSenderConfig(AppConfig):
    name = 'admin_email_sender'
    verbose_name = 'Admin Email Sender'

    def ready(self):
        import admin_email_sender.signals
