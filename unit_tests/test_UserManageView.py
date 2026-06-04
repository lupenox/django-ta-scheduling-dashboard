from django.test import TestCase
from django.contrib.auth.models import User

class ListUserTests(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='testuser1', password='password123')
        self.user2 = User.objects.create_user(username='testuser2', password='password123')

    def test_list_users(self):
        users = User.objects.all()
        self.assertIn(self.user1, users)
        self.assertIn(self.user2, users)

# Testing user creation
class CreateUserTests(TestCase):
    def setUp(self):
        User.objects.create_user(username='admin', password='12345')
        self.client.login(username='admin', password='12345')

    def test_create_user_valid(self):
        User.objects.create_user(username='newuser', password='newpass')
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_create_user_invalid(self):
        # Attempt to create a user without a username
        try:
            User.objects.create_user(username='', password='pass')
            user_created = True
        except:
            user_created = False
        self.assertFalse(user_created)

# Testing user update
class UpdateUserTests(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(username='testuser', password='12345')

    def test_update_user_valid(self):
        # Update the user's password
        self.test_user.set_password('newpassword123')
        self.test_user.save()
        self.test_user.refresh_from_db()
        self.assertTrue(self.test_user.check_password('newpassword123'))

# Testing user deletion
class DeleteUserTests(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(username='testuser', password='12345')

    def test_delete_user_valid(self):
        username = self.test_user.username
        User.objects.filter(username=username).delete()
        self.assertFalse(User.objects.filter(username=username).exists())
