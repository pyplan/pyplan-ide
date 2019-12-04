from django.contrib import admin
from pyplan.pyplan.common.email.models import EmailQueue

@admin.register(EmailQueue)
class EmailQueueAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject', 'created_at', 'email_from', 'name_from',
                    'email_to', 'name_to', 'date_sent', 'retries', 'email_type', 'context', 'usercompany_id')
