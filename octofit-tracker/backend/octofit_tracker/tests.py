from django.test import TestCase
from .models import Team, CustomUser, Activity, Workout, Leaderboard

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(str(team), 'Test Team')

class CustomUserModelTest(TestCase):
    def test_create_user(self):
        team = Team.objects.create(name='Test Team')
        user = CustomUser.objects.create_user(username='testuser', email='test@example.com', password='pass', team=team)
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.team, team)

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        team = Team.objects.create(name='Test Team')
        user = CustomUser.objects.create_user(username='testuser', email='test@example.com', password='pass', team=team)
        activity = Activity.objects.create(user=user, type='run', duration=30, distance=5)
        self.assertEqual(activity.type, 'run')

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name='Test Workout', description='desc')
        self.assertEqual(workout.name, 'Test Workout')

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        team = Team.objects.create(name='Test Team')
        user = CustomUser.objects.create_user(username='testuser', email='test@example.com', password='pass', team=team)
        leaderboard = Leaderboard.objects.create(user=user, points=100)
        self.assertEqual(leaderboard.points, 100)
