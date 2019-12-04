from django.db import migrations, models


def update_default_email_preferences(apps, schema_editor):

    PreferenceModule = apps.get_model('pyplan', 'PreferenceModule')
    Preference = apps.get_model('pyplan', 'Preference')

    # EMAILSETTINGS
    pref_mod_3 = PreferenceModule.objects.get(code='email_settings')

    # host
    email_smtp_host = Preference.objects.get(
        module=pref_mod_3, code='smtp_host')
    email_smtp_host.definition['value'] = 'smtpout.secureserver.net'
    email_smtp_host.save()

    # port
    email_smtp_port = Preference.objects.get(
        module=pref_mod_3, code='smtp_port')
    email_smtp_port.definition['value'] = 465
    email_smtp_port.save()

    # user
    email_smtp_user = Preference.objects.get(
        module=pref_mod_3, code='smtp_user')
    email_smtp_user.definition['value'] = 'info@pyplan.com'
    email_smtp_user.save()

    # password
    email_smtp_password = Preference.objects.get(
        module=pref_mod_3, code='smtp_password')
    email_smtp_password.definition['value'] = 'nvxValpa3540'
    email_smtp_password.save()

    # from name
    email_default_from_name = Preference.objects.get(
        module=pref_mod_3, code='email_default_from_name')
    email_default_from_name.definition['value'] = 'No Reply - Pyplan Info'
    email_default_from_name.save()

    # use tls
    email_use_tls = Preference.objects.get(
        module=pref_mod_3, code='smtp_use_tls')
    email_use_tls.definition['value'] = False
    email_use_tls.save()

    # use ssl
    email_use_ssl = Preference.objects.get(
        module=pref_mod_3, code='smtp_use_ssl')
    email_use_ssl.definition['value'] = True
    email_use_ssl.save()


def update_pyplan_email_preferences(apps, schema_editor):

    CompanyPreference = apps.get_model('pyplan', 'CompanyPreference')

    # - get company
    Company = apps.get_model('pyplan', 'Company')
    company = Company.objects.get(code='pyplan')

    # - get preferences
    Preference = apps.get_model('pyplan', 'Preference')
    smtp_host = Preference.objects.get(code='smtp_host')
    smtp_port = Preference.objects.get(code='smtp_port')
    smtp_user = Preference.objects.get(code='smtp_user')
    smtp_password = Preference.objects.get(code='smtp_password')
    smtp_default_from_name = Preference.objects.get(
        code='email_default_from_name')
    smtp_use_tls = Preference.objects.get(code='smtp_use_tls')
    smtp_use_ssl = Preference.objects.get(code='smtp_use_ssl')

    # host
    email_smtp_host = CompanyPreference.objects.get(
        company=company, preference=smtp_host)
    email_smtp_host.definition['value'] = 'smtpout.secureserver.net'
    email_smtp_host.save()

    # port
    email_smtp_port = CompanyPreference.objects.get(
        company=company, preference=smtp_port)
    email_smtp_port.definition['value'] = 465
    email_smtp_port.save()

    # user
    email_smtp_user = CompanyPreference.objects.get(
        company=company, preference=smtp_user)
    email_smtp_user.definition['value'] = 'info@pyplan.com'
    email_smtp_user.save()

    # password
    email_smtp_password = CompanyPreference.objects.get(
        company=company, preference=smtp_password)
    email_smtp_password.definition['value'] = 'nvxValpa3540'
    email_smtp_password.save()

    # from name
    email_default_from_name = CompanyPreference.objects.get(
        company=company, preference=smtp_default_from_name)
    email_default_from_name.definition['value'] = 'No Reply - Pyplan Info'
    email_default_from_name.save()

    # use tls
    email_use_tls = CompanyPreference.objects.get(
        company=company, preference=smtp_use_tls)
    email_use_tls.definition['value'] = False
    email_use_tls.save()

    # use ssl
    email_use_ssl = CompanyPreference.objects.get(
        company=company, preference=smtp_use_ssl)
    email_use_ssl.definition['value'] = True
    email_use_ssl.save()


class Migration(migrations.Migration):

    dependencies = [
        ('pyplan', '0005_inputtemplate'),
    ]

    operations = [
        migrations.RunPython(update_default_email_preferences),
        migrations.RunPython(update_pyplan_email_preferences),
    ]
