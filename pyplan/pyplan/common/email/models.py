import uuid
from django.db import models

from pyplan.pyplan.usercompanies.models import UserCompany

class EmailQueue(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    subject = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now=True)
    email_from = models.EmailField(null=False)
    name_from = models.TextField(null=False)
    email_to = models.EmailField(null=False)
    name_to = models.TextField(null=False)
    date_sent = models.DateTimeField(null=True)
    retries = models.IntegerField(default=0)
    email_type = models.IntegerField(null=False)
    context = models.TextField(null=True)
    usercompany = models.ForeignKey(UserCompany, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.date_sent} -Subject: {self.subject} / From: {self.email_from} - {self.name_from} / To: {self.email_to} - {self.name_to} / Type: {self.email_type}  / Context: {self.context}"
