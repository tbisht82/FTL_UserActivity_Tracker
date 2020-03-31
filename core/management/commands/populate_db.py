from django.utils import timezone
from datetime import timedelta
import random
import pytz

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from core.models import ActivityPeriod


def populate_database():
    """
    This function loads dummy data into user and activity_period tables in db.
    User can provide number of dummy users need to be created in command line or it will create 3 dummy users.
    command: python manage.py populate_db --> this will create 3 dummy users in db
    command: python manage.py populate_db --users <number_of_users> --> this will create <number_of_users> users
    """

    timezone_choice = list(pytz.all_timezones_set)

    user = get_user_model()
    email = "test"+str(random.randint(100, 10000))+"@"+"test"+".com"
    name = "test"+str(random.randint(100, 500))+" surname"+str(random.randint(1, 50))
    u = user.objects.create(email=email)
    u.name = name
    u.set_password('Test@1234')
    r = random.randint(0, len(timezone_choice))
    u.timezone = timezone_choice[r]
    u.save()

    for i in range(0, random.randint(2, 6)):
        s = timezone.now() - timedelta(days=random.randint(0, 29), minutes=random.randint(10, 60))
        e = s + timedelta(minutes=random.randint(30, 200))
        act = ActivityPeriod.objects.create(start_time=s,
                                            end_time=e,
                                            user=u)
        act.save()


class Command(BaseCommand):
    help = 'Load dummy data into the database'

    def add_arguments(self, parser):
        parser.add_argument('--users',
                            default=3,
                            type=int,
                            help='Number of users to create.')

    def handle(self, *args, **options):
        for _ in range(options['users']):
            populate_database()
