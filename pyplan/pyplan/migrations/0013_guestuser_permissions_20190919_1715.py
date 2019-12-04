from django.contrib.contenttypes.management import (
    create_contenttypes, get_contenttypes_and_models)
from django.db import migrations


def update_guest_groups_permissions(apps, schema_editor):
    """
    This migration adds necessary permissions to guest groups.
    """

    Dashboard = apps.get_model('pyplan', 'Dashboard')
    InputTemplate = apps.get_model('pyplan', 'InputTemplate')
    Group = apps.get_model('auth', 'Group')
    Permission = apps.get_model('auth', 'Permission')
    ContentType = apps.get_model('contenttypes', 'ContentType')

    content_types, app_models = get_contenttypes_and_models(
        apps.app_configs['pyplan'], 'default', ContentType)

    # If content_types are not created yet, then it's a clean install.
    # In order to add permissions after, we need to force ContentType creation.
    if not content_types:
        create_contenttypes(apps.app_configs['pyplan'])

    # Dashboard content type
    ctype_dashboard = ContentType.objects.get_for_model(Dashboard)

    # Dashboard permissions
    view_dashboard_perm, view_dash_perm_created = Permission.objects.get_or_create(
        codename='view_dashboard',
        content_type=ctype_dashboard,
    )
    if view_dash_perm_created:
        view_dashboard_perm.name = 'Can view dashboard'
        view_dashboard_perm.save()

    change_dashboard_perm, change_dash_perm_created = Permission.objects.get_or_create(
        codename='change_dashboard',
        content_type=ctype_dashboard,
    )
    if change_dash_perm_created:
        change_dashboard_perm.name = 'Can change dashboard'
        change_dashboard_perm.save()

    # InputTemplate content type
    ctype_inputtemplate = ContentType.objects.get_for_model(InputTemplate)

    # InputTemplate permissions
    view_inputtemplate_perm, view_inptmp_created = Permission.objects.get_or_create(
        codename='view_inputtemplate',
        content_type=ctype_inputtemplate,
    )
    if view_inptmp_created:
        view_inputtemplate_perm.name = 'Can view input template'
        view_inputtemplate_perm.save()

    change_inputtemplate_perm, change_inptmp_created = Permission.objects.get_or_create(
        codename='change_inputtemplate',
        content_type=ctype_inputtemplate,
    )
    if change_inptmp_created:
        change_inputtemplate_perm.name = 'Can change input template'
        change_inputtemplate_perm.save()

    guest_groups = Group.objects.filter(name__icontains='guest')

    for guest_group in guest_groups:
        guest_group.permissions.add(view_dashboard_perm)
        guest_group.permissions.add(change_dashboard_perm)
        guest_group.permissions.add(view_inputtemplate_perm)
        guest_group.permissions.add(change_inputtemplate_perm)
        guest_group.save()


class Migration(migrations.Migration):

    dependencies = [
        ('pyplan', '0012_new_email_preferences_20190824'),
    ]

    operations = [
        migrations.RunPython(update_guest_groups_permissions),
    ]
