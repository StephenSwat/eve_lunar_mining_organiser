from django.core.management.base import BaseCommand
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType


class Command(BaseCommand):
    help = 'Creates permissions on the EVE SDE for Django Guardian.'

    def handle(self, *args, **options):
        ct_region = ContentType.objects.get(app_label='eve_sde', model='region')
        ct_constellation = ContentType.objects.get(app_label='eve_sde', model='constellation')
        ct_solarsystem = ContentType.objects.get(app_label='eve_sde', model='solarsystem')

        for cn, ct in [
            ('reg', ct_region),
            ('con', ct_constellation),
            ('sys', ct_solarsystem)
        ]:
            Permission.objects.create(
                codename=cn + '_can_view_scans',
                name='Can view all scans in this location',
                content_type=ct
            )

            Permission.objects.create(
                codename=cn + '_can_add_scans',
                name='Can add new scans in this location',
                content_type=ct
            )

            Permission.objects.create(
                codename=cn + '_can_delete_scans',
                name='Can delete other people\'s scans in this location',
                content_type=ct
            )
