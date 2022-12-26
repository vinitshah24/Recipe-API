"""
Django command - Waits for the database to be available
"""
import time

from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django command to pause execution until database is available"""

    def handle(self, *args, **options):
        """ Django command to wait for database """
        self.stdout.write('Waiting for database...')
        is_db_running = False

        while not is_db_running:
            try:
                self.check(databases=["default"])
                is_db_running = True
            except OperationalError:
                self.stdout.write("Database unavailable, waiting for 1 second...")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database available!'))
