from django.contrib import admin

from admin_email_sender.models import SendEmail, Template


@admin.register(SendEmail)
class SendEmailLogin(admin.ModelAdmin):
    filter_horizontal = ('users',)

    list_display = ('subject', 'template', 'created_at', 'total_emails', 'status',)

    def total_emails(self, obj):
        return obj.users.count()


@admin.register(Template)
class TemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at',)
