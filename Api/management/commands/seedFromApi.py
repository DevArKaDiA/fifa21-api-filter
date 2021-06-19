from django.core.management.base import BaseCommand, CommandError, CommandParser
from Api.models import Player


class Command(BaseCommand):
    help = "Seed players from 3 party API"

    def add_arguments(self, parser):
        parser.add_argument('flush', nargs='+', type=int)

    def handle(self, *args, **options):
        pass
        # for poll_id in options['poll_ids']:
        #     try:
        #         poll = Poll.objects.get(pk=poll_id)
        #     except Poll.DoesNotExist:
        #         raise CommandError('Poll "%s" does not exist' % poll_id)

        #     poll.opened = False
        #     poll.save()

        #     self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))