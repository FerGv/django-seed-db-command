"""Seed DB command."""

# Python
import os

# Django
from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    """Load all apps' fixtures."""

    help = 'Load all apps\' fixtures.'

    def handle(self, *args, **options):
        """Search fixtures folder and load files into them."""

        fixtures = []

        try:
            for root, dirs, files in os.walk(settings.BASE_DIR):
                for name in files:
                    if 'fixtures' in root and name != '__init__.py':
                        fixtures.append(name)

            call_command('loaddata', *fixtures)
        except Exception as e:
            raise CommandError(
                f'An error has ocurred while loading fixtures. \n{e}'
            )

        self.stdout.write(self.style.SUCCESS('Fixtures have been loaded'))
