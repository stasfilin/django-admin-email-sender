from django.contrib import admin
from .models import SendEmail


@admin.register(SendEmail)
class SendEmailLogin(admin.ModelAdmin):

    filter_horizontal = ('users',)

    list_display = ('subject', 'total_emails', 'status',)

    def total_emails(self, obj):
        return obj.users.count()
