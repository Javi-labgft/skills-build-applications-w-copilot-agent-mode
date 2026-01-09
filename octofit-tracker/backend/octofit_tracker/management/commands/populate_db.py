from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from django.utils import timezone
from pymongo import MongoClient

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        self.stdout.write('Deleting old data...')
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()

        self.stdout.write('Creating teams...')

        Team.objects.create(name='marvel', description='Marvel superheroes')
        Team.objects.create(name='dc', description='DC superheroes')

        self.stdout.write('Creating users...')
        users = [
            User.objects.create(email='ironman@marvel.com', name='Iron Man', team='marvel', is_superhero=True),
            User.objects.create(email='spiderman@marvel.com', name='Spider-Man', team='marvel', is_superhero=True),
            User.objects.create(email='batman@dc.com', name='Batman', team='dc', is_superhero=True),
            User.objects.create(email='wonderwoman@dc.com', name='Wonder Woman', team='dc', is_superhero=True),
        ]

        self.stdout.write('Creating activities...')
        Activity.objects.create(user_email='ironman@marvel.com', type='run', duration=30, date=timezone.now())
        Activity.objects.create(user_email='spiderman@marvel.com', type='swim', duration=45, date=timezone.now())
        Activity.objects.create(user_email='batman@dc.com', type='cycle', duration=60, date=timezone.now())
        Activity.objects.create(user_email='wonderwoman@dc.com', type='yoga', duration=50, date=timezone.now())

        self.stdout.write('Creating workouts...')
        Workout.objects.create(name='Pushups', description='Do 20 pushups', suggested_for='marvel')
        Workout.objects.create(name='Situps', description='Do 30 situps', suggested_for='dc')

        self.stdout.write('Creating leaderboard...')
        Leaderboard.objects.create(team_name='marvel', points=150)
        Leaderboard.objects.create(team_name='dc', points=120)

        self.stdout.write('Ensuring unique index on email for users...')
        client = MongoClient('mongodb://localhost:27017')
        db = client['octofit_db']
        db.users.create_index([('email', 1)], unique=True)
        self.stdout.write(self.style.SUCCESS('Database populated with test data!'))
