from django.test import TestCase
from django.contrib.auth.models import User

class UserProfile(TestCase):

    def test_create_user_should_create_userprofile(self):
        test_username = "test_user"
        test_password = "test_password"
        test_user = User.objects.create_user(
            usernmae=test_username,
            password=test_password,
        )
