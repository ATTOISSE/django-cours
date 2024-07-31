from django.core.management.base import BaseCommand,CommandError, CommandParser
from django.contrib.auth.models import Group

class Command(BaseCommand):
    help = 'permet de creer un groupe'

    def add_arguments(self, parser: CommandParser)-> None:
        parser.add_argument('group_names',nargs='+',type=str)

    def handle(self, *args, **options) -> str | None:
        group_names = options['group_names']
        for group_name in group_names:
            name,created = Group.objects.get_or_create(
                name = group_name
            )
            if not created:
                raise CommandError(f'Le groupe {group_name} existe deja')
            self.stdout.write(
                self.style.SUCCESS(f'le Groupe {group_name} a été crée avec succes')
            )
    