from django.core.management.base import BaseCommand,CommandError, CommandParser
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from orders.models import Product

class Command(BaseCommand):
    help = "Permet de créer une permission aux utilisateurs"

    def add_arguments(self, parser):
        parser.add_argument("permission_names", nargs="+", type=str)

    def handle(self, *args, **options):
        permission_names = options["permission_names"]
        content_type = ContentType.objects.get_for_model(Product)
        for permission_name in permission_names:
            _, created = Permission.objects.get_or_create(
                name=f"Can perform operation corresponding to {permission_name}",
                content_type=content_type,
                codename=permission_name
            )
            if not created:
                raise CommandError(f'La permission avec le nom {permission_name} existe déjà')

            self.stdout.write(
                self.style.SUCCESS(f'La permission {permission_name} a été créée avec succès')
            )