import uuid

from django.conf import settings
from django.contrib.auth.models import AbstractUser, Permission
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    active = models.BooleanField(default=True)
    system = models.BooleanField(default=False)
    langCode = models.CharField(max_length=10, null=True)
    imageURL = models.CharField(max_length=200, null=True)
    fromAD = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    companies = models.ManyToManyField('Company', through='UserCompany')

    def get_user_permissions(self):
        """
        Return all permisions of the user. User-permissions and group-permissions 
        """
        if self.is_superuser:
            return list(set(Permission.objects.values_list('codename', flat=True)))
        return list(set(self.user_permissions.values_list('codename', flat=True) | Permission.objects.filter(group__user=self).values_list('codename', flat=True)))

    class Meta:
        app_label = 'pyplan'
        verbose_name = 'user'
        verbose_name_plural = 'users'

        permissions = (
            # # Security / Sessions
            # "GETALLSESSIONS"
            ("list_sessions", "Can list sessions"),
            # "GETCOMPANYSESSIONS"
            ("list_company_sessions", "Can get company sessions"),
            # "KILLSESSIONS"
            ("kill_sessions", "Can kill sessions"),
            # "SANITYCHECK"
            ("do_sanity_check", "Can do sanity check"),
            # "EDITPROFILE"
            ("change_profile", "Can change profile"),
            # "USERSTATS"
            ("get_user_stats", "Can get user stats"),
            # "LICENCEINFO"
            ("get_licence_info", "Can get licence info"),

            # # File Manager
            ("add_folder", "Can add folders"),
            ("copy_file_or_folder", "Can copy file or folder"),
            ("delete_files", "Can delete files or folders"),
            # "GETFILES"
            ("list_folders", "Can list folders"),
            # "GETMODELPATHROOT"
            ("view_model_path_root", "Can view model path root"),
            # "GETCOMPANYROOT"
            ("view_company_root", "Can view company root"),
            # "SETDEFAULTCOMPANYMODEL"
            ("change_default_company_model", "Can change default company model"),
            # "CREATEPUBLIC"
            ("add_file_public", "Can create file in public folder"),
            # "RENAMEPUBLIC"
            ("change_file_name_public", "Can rename file in public folder"),
            # "DELETEPUBLIC"
            ("delete_file_public", "Can delete file in public folder"),
            # "COPYTOMYWORKSPACE"
            ("copy_model_to_my_workspace", "Can copy model to my workspace"),
            # "DOWNLOADFILES"
            ("download_files", "Can download files"),
            # "UPLOADPUBLIC"
            ("upload_file_public", "Can upload file in Public folder"),

            # # Influence Diagram
            # "INFLUENCEDIAGRAM"
            ("view_influence_diagram", "Can view influence diagram"),
            # "EDITMODEL"
            ("change_influence_diagram", "Can edit influence diagram"),
            # "SETGROUPPERMISSIONS"
            ("change_group_permissions", "Can change group permissions"),

            # # Model Manager
            # "SAVEMODEL"
            ("change_model", "Can change model"),
            # "SAVEMODELINPUBLIC"
            ("change_public_model", "Can change model in public folder"),
            # "VIEWALLMODELFUNCTIONS"
            ("list_model_functions", "Can list model functions"),
            # "LASTMODELS"
            ("list_last_models", "Can list last models"),

            # # Data Snapshots
            # "MANAGEDATASNAPSHOTS"
            ("change_data_snapshots", "Can change data snapshots"),

            # # User Manager
            # "GETUSER" -> view_user
            # "CREATEUSER" -> add_user
            # "LISTUSERS"
            ("list_users", "Can list user"),
            # "UPDATEUSER" -> change_user
            # "DELETEUSER" -> delete_user
            # "LOGINASOTHERUSER"
            ("impersonate_user", "Login as other user"),

            # # Form Manager
            # "GETFORM"
            ("view_form", "Can view form"),
            # "CREATEFORM"
            ("add_form", "Create add form"),
            # "LISTFORMS"
            ("list_forms", "Can list forms"),
            # "UPDATEFORM"
            ("change_form", "Can change form"),
            # "DELETEFORM"
            ("delete_form", "Can delete form"),
            # "GENERATEFORM"
            ("add_form_entity", "Can add form entity"),
            # "DROPFORM"
            ("delete_form_entity", "Can drop form entity"),
            # "GETDATAENTITY"
            ("view_entity_data", "Can view entity data"),
            # "INSERTDATAENTITY"
            ("add_entity_data", "Can add entity data"),
            # "UPDATEDATAENTITY"
            ("change_entity_data", "Can change entity data"),
            # "DELETEDATAENTITY"
            ("delete_entity_data", "Can delete entity data"),

            # # Others
            # "VIEWSYSTEMFUNCTIONS"
            ("view_system_functions", "Can view system functions"),
        )


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
