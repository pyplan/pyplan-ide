# models
from pyplan.pyplan.company_preference.models import CompanyPreference
from pyplan.pyplan.preference.models import Preference

# enums
from pyplan.pyplan.common.email.classes.eEmailType import eEmailType

class Email(object):

    def __init__(self, **kargs):
        self.id = kargs["id"] if "id" in kargs else None
        self.subject = kargs["subject"] if "subject" in kargs else None
        self.created_at = kargs["created_at"] if "created_at" in kargs else None
        self.email_from = kargs["email_from"] if "email_from" in kargs else None
        self.name_from = kargs["name_from"] if "name_from" in kargs else None
        self.email_to = kargs["email_to"] if "email_to" in kargs else None
        self.name_to = kargs["name_to"] if "name_to" in kargs else None
        self.date_sent = kargs["date_sent"] if "date_sent" in kargs else None
        self.retries = kargs["retries"] if "retries" in kargs else None
        self.email_type = kargs["email_type"] if "email_type" in kargs else None
        self.context = kargs["context"] if "context" in kargs else None
        self.usercompany_id = kargs["usercompany_id"] if "usercompany_id" in kargs else {}
