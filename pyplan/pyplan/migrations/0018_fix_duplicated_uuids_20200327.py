# Generated by Django 2.2.5 on 2020-03-27

import uuid

from django.db import migrations, models


def create_uuid(apps, schema_editor):
    Dashboard = apps.get_model('pyplan', 'Dashboard')
    dashboards = Dashboard.objects.all()
    for index, dashboard in enumerate(dashboards):
        if index == 17:
            break
        dashboard.uuid = uuid.uuid4()
        dashboard.save()

    Report = apps.get_model('pyplan', 'Report')
    reports = Report.objects.all()
    for index, report in enumerate(reports):
        if index == 3:
            break
        report.uuid = uuid.uuid4()
        report.save()

class Migration(migrations.Migration):

    dependencies = [
        ('pyplan', '0017_user_my_uuid_my_username_20200205_1454'),
    ]

    operations = [
        migrations.RunPython(create_uuid),
    ]
