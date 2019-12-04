import os
import json
import datetime
import requests
from django.core.mail import EmailMultiAlternatives, send_mass_mail, get_connection
from django.template.loader import render_to_string
from rest_framework import exceptions
from pyplan.pyplan.common.baseService import BaseService

# models
from pyplan.pyplan.company_preference.models import CompanyPreference
from pyplan.pyplan.preference.models import Preference
from pyplan.pyplan.common.email.models import EmailQueue

# classes
from pyplan.pyplan.common.email.classes.email import Email

# enums
from pyplan.pyplan.common.email.classes.eEmailType import eEmailType


class EmailService(BaseService):

    def addToQueue(self, email):
        """
        Adds an email object to the queue and automatically sends it
        """
        ###########
        # EXAMPLE #
        ###########
        # This sends a test email, the context are the variables that the template expects
        ###########
        # from pyplan.pyplan.common.email.service import EmailService
        # from pyplan.pyplan.common.email.classes.eEmailType import eEmailType
        # email = {
        #    'email_to': 'mnallino@pyplan.com',
        #    'name_to': 'Mr. CardCaptor',
        #    'email_type': eEmailType.TEST,
        #    'context': {"username": "CardCaptor"}
        # }
        # service = EmailService(request)
        # service.addToQueue(email)
        try:
            if self._getCompanyPreference('email_service_active'):

                oEmail = Email(**email)
                oEmail.email_type = eEmailType(oEmail.email_type.value)
                oEmail.subject = self._getSubjectFromEmailType(
                    oEmail.email_type) if not oEmail.subject else oEmail.subject
                oEmail.email_from = self._getCompanyPreference(
                    'smtp_user') if not oEmail.email_from else oEmail.email_from
                oEmail.name_from = self._getCompanyPreference(
                    'email_default_from_name') if not oEmail.name_from else oEmail.name_from
                # In case we don't have a session like in reset password cases
                oEmail.usercompany_id = 1
                if self.client_session:
                    oEmail.usercompany_id = self.client_session.userCompanyId

                result = EmailQueue.objects.create(
                    subject=oEmail.subject,
                    email_from=oEmail.email_from,
                    name_from=oEmail.name_from,
                    email_to=oEmail.email_to,
                    name_to=oEmail.name_to,
                    email_type=oEmail.email_type.value,
                    context=json.dumps(oEmail.context),
                    usercompany_id=oEmail.usercompany_id
                )
                return True
            return False
        except Exception as ex:
            raise exceptions.NotAcceptable(
                f"Error in EmailQueueService.addToQueue(): {str(ex)}")

    def sendQueue(self, throwError=False):
        """
        Sends all emails in the queue
        """
        if self._getCompanyPreference('email_service_active'):
            throwError = self._getCompanyPreference('email_throw_errors')
            emailQueue = EmailQueue.objects.filter(date_sent__isnull=True)
            if self._getCompanyPreference('email_use_smtp'):
                # sends email thought smtp server
                for email in emailQueue:
                    try:
                        context = json.loads(email.context)
                        template = self._getTemplateFromEmailType(
                            eEmailType(email.email_type), context=context)
                        message = {
                            'subject': email.subject,
                            'html_content': template,
                            'from_email': f"{email.name_from} <{email.email_from}>",
                            'recipients': [f"{email.name_to} <{email.email_to}>"],
                            'throwError': throwError
                        }
                        if self._send_email(**message):
                            email.date_sent = datetime.datetime.now()
                            email.save()
                        else:
                            # error ocurred will save later
                            email.retries = email.retries + 1
                            email.save()
                        return True
                    except Exception as ex:
                        if throwError:
                            email.retries = email.retries + 1
                            email.save()
                            raise exceptions.NotAcceptable(
                                f"Error in EmailQueueService.sendQueue() using SMTP: {str(ex)}")
                        else:
                            email.retries = email.retries + 1
                            email.save()
                            pass
            else:
                # sends email thought elasticmail api
                api_uri = os.getenv('EMAIL_API_URI')
                api_user = os.getenv('EMAIL_API_USER')
                api_key = os.getenv('EMAIL_API_KEY')
                for email in emailQueue:
                    try:
                        con = json.loads(email.context)
                        context = self._change_keys_for_API(con)
                        template = self._getTemplateFromEmailType(
                            eEmailType(email.email_type), context=context, forSMTP=False)
                        context['template'] = template
                        context['username'] = api_user
                        context['api_key'] = api_key
                        context['from'] = email.email_from
                        context['from_name'] = email.name_from
                        context['to'] = email.email_to
                        context['subject'] = email.subject
                        context['encodingtype'] = 0
                        result = self._post(api_uri, data=context)
                        if result:
                            if len(result) > 0:
                                email.date_sent = datetime.datetime.now()
                                email.save()
                            else:
                                # error ocurred will save later
                                email.retries = email.retries + 1
                                email.save()
                        else:
                            # error ocurred will save later
                            email.retries = email.retries + 1
                            email.save()
                        return True
                    except Exception as ex:
                        if throwError:
                            email.retries = email.retries + 1
                            email.save()
                            raise exceptions.NotAcceptable(
                                f"Error in EmailQueueService.sendQueue() using API : {str(ex)}")
                        else:
                            email.retries = email.retries + 1
                            email.save()
                            pass
            return False

        else:
            return True

    def _post(self, url, data):
        response = requests.post(url=url, data=data)
        response.raise_for_status()
        return response.text

    # Helper functions

    def _getCompanyPreference(self, code):
        preference = Preference.objects.filter(code=code).first()
        if preference:
            if self.client_session:
                company_id = self.client_session.companyId
                c_pref = CompanyPreference.objects.filter(
                    company_id=company_id, preference__code=code).first()
                if c_pref:
                    if c_pref.definition:
                        preference.definition = c_pref.definition
        if preference.definition:
            return preference.definition['value']
        else:
            return None

    def _getSubjectFromEmailType(self, emailType):
        if emailType.value == eEmailType.WORKFLOW_ASSIGNED_TASK.value:
            return "You have a new assignment"
        elif emailType.value == eEmailType.WORKFLOW_CHANGE_STATE.value:
            return "Your assignment status has changed"
        elif emailType.value == eEmailType.WORKFLOW_CHANGE_PERCENT.value:
            return "Your assignment percent has changed"
        elif emailType.value == eEmailType.INTERFACE_COMMENT.value:
            return "You have a new comment in your interface"
        elif emailType.value == eEmailType.INTERFACE_REFRESH_USER_IN_COMMENT.value:
            return "Someone has mention you in a comment"
        elif emailType.value == eEmailType.INTERFACE_SHARED.value:
            return "A interface has been shared with you"
        elif emailType.value == eEmailType.APPLICATION_SHARED.value:
            return "An application has been shared with you"
        elif emailType.value == eEmailType.RESET_PASSWORD.value:
            return "Reset your Pyplan password"
        elif emailType.value == eEmailType.CHANGED_PASSWORD.value:
            return "Your Pyplan password has changed"
        elif emailType.value == eEmailType.TEST.value:
            return "Pyplan test email"
        elif emailType.value == eEmailType.WELCOME_USER.value:
            return "Welcome to Pyplan!"
        elif emailType.value == eEmailType.CREATED_USER.value:
            return "A new user has been created"
        elif emailType.value == eEmailType.ACTIVATED_USER.value:
            return "Your account has been activated"
        elif emailType.value == eEmailType.SCHEDULE_TASK_STATUS_CHANGED.value:
            return "A task status has changed"
        elif emailType.value == eEmailType.DEACTIVATED_USER.value:
            return "Your account has been deactivated"

    def _getTemplateFromEmailType(self, emailType, context={}, forSMTP=True):
        template_prefix = self._getCompanyPreference('email_template_prefix')
        if forSMTP:
            if emailType.value == eEmailType.WORKFLOW_ASSIGNED_TASK.value:
                return self._get_rendered_html(template_prefix + "assignedtask.html", context=context)
            elif emailType.value == eEmailType.WORKFLOW_CHANGE_STATE.value:
                return self._get_rendered_html(template_prefix + "changetaskstate.html", context=context)
            elif emailType.value == eEmailType.WORKFLOW_CHANGE_PERCENT.value:
                return self._get_rendered_html(template_prefix + "changetaskpercent.html", context=context)
            elif emailType.value == eEmailType.INTERFACE_COMMENT.value:
                return self._get_rendered_html(template_prefix + "interfacecomment.html", context=context)
            elif emailType.value == eEmailType.INTERFACE_REFRESH_USER_IN_COMMENT.value:
                return None  # TODO: Implement this
            elif emailType.value == eEmailType.INTERFACE_SHARED.value:
                return self._get_rendered_html(template_prefix + "sharedinterface.html", context=context)
            elif emailType.value == eEmailType.APPLICATION_SHARED.value:
                return self._get_rendered_html(template_prefix + "sharedapplication.html", context=context)
            elif emailType.value == eEmailType.RESET_PASSWORD.value:
                return self._get_rendered_html(template_prefix + "resetpassword.html", context=context)
            elif emailType.value == eEmailType.CHANGED_PASSWORD.value:
                return self._get_rendered_html(template_prefix + "changedpassword.html", context=context)
            elif emailType.value == eEmailType.TEST.value:
                return self._get_rendered_html(template_prefix + "testemail.html", context=context)
            elif emailType.value == eEmailType.WELCOME_USER.value:
                return self._get_rendered_html(template_prefix + "welcome.html", context=context)
            elif emailType.value == eEmailType.CREATED_USER.value:
                return self._get_rendered_html(template_prefix + "createduser.html", context=context)
            elif emailType.value == eEmailType.ACTIVATED_USER.value:
                return self._get_rendered_html(template_prefix + "activateduser.html", context=context)
            elif emailType.value == eEmailType.SCHEDULE_TASK_STATUS_CHANGED.value:
                return self._get_rendered_html(template_prefix + "scheduletaskstatus.html", context=context)
            elif emailType.value == eEmailType.DEACTIVATED_USER.value:
                return self._get_rendered_html(template_prefix + "deactivateduser.html", context=context)
        else:
            if emailType.value == eEmailType.WORKFLOW_ASSIGNED_TASK.value:
                return template_prefix + "assignedtask"
            elif emailType.value == eEmailType.WORKFLOW_CHANGE_STATE.value:
                return template_prefix + "changetaskstate"
            elif emailType.value == eEmailType.WORKFLOW_CHANGE_PERCENT.value:
                template_prefix + "changetaskpercent"
            elif emailType.value == eEmailType.INTERFACE_COMMENT.value:
                return template_prefix + "interfacecomment"
            elif emailType.value == eEmailType.INTERFACE_REFRESH_USER_IN_COMMENT.value:
                return None  # TODO: Implement this
            elif emailType.value == eEmailType.INTERFACE_SHARED.value:
                return template_prefix + "sharedinterface"
            elif emailType.value == eEmailType.APPLICATION_SHARED.value:
                return template_prefix + "sharedapplication"
            elif emailType.value == eEmailType.RESET_PASSWORD.value:
                return template_prefix + "resetpassword"
            elif emailType.value == eEmailType.CHANGED_PASSWORD.value:
                return template_prefix + "changedpassword"
            elif emailType.value == eEmailType.TEST.value:
                return template_prefix + "testemail"
            elif emailType.value == eEmailType.WELCOME_USER.value:
                return template_prefix + "welcome"
            elif emailType.value == eEmailType.CREATED_USER.value:
                return template_prefix + "createduser"
            elif emailType.value == eEmailType.ACTIVATED_USER.value:
                return template_prefix + "activateduser"
            elif emailType.value == eEmailType.SCHEDULE_TASK_STATUS_CHANGED.value:
                return template_prefix + "scheduletaskstatus"
            elif emailType.value == eEmailType.DEACTIVATED_USER.value:
                return template_prefix + "deactivateduser"

    def _get_rendered_html(self, template_name, context={}):
        html_content = render_to_string(template_name, context)
        return html_content

    def _send_email(self, subject, html_content, text_content='', from_email=None, recipients=[], attachments=[], bcc=[], cc=[], throwError=False):
        try:
            connection = get_connection(
                host=self._getCompanyPreference('smtp_host'),
                port=self._getCompanyPreference('smtp_port'),
                username=self._getCompanyPreference('smtp_user'),
                password=self._getCompanyPreference('smtp_password'),
                use_tls=self._getCompanyPreference('smtp_use_tls'),
                use_ssl=self._getCompanyPreference('smtp_use_ssl'),
                timeout=self._getCompanyPreference('smtp_timeout'),
                ssl_keyfile=self._getCompanyPreference('smtp_ssl_keyfile'),
                ssl_certfile=self._getCompanyPreference('smtp_ssl_certfile'),
                fail_silently=throwError
            )
            # send email to user with attachment
            email = EmailMultiAlternatives(
                subject,
                text_content,
                from_email,
                recipients,
                bcc=bcc,
                cc=cc,
                connection=connection
            )
            email.attach_alternative(html_content, "text/html")
            for attachment in attachments:
                # Example: email.attach('design.png', img_data, 'image/png')
                email.attach(*attachment)
            email.send(fail_silently=throwError)
            return True
        except Exception as ex:
            if throwError:
                raise exceptions.NotAcceptable(
                    f"Error in EmailQueueService._send_email(): {str(ex)}")
            else:
                return False

    def _change_keys_for_API(self, obj):
        for key in obj.keys():
            new_key = "merge_" + key
            if key[:6] != "merge_":
                obj[new_key] = obj[key]
                del obj[key]
        return obj
