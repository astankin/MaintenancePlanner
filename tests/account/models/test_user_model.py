from django.core.exceptions import ValidationError
from django.test import TestCase
from django.contrib.auth import get_user_model

from MaintenancePlanner.accounts.models import Profile
from MaintenancePlanner.accounts.validators import user_name_validator

User = get_user_model()


class UserCreationTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='password',
            first_name='Atanas',
            last_name='Stankin',
            email='astankin@abv.bg',
            role='MANAGER'
        )

    def test_if_user_is_created(self):
        self.assertTrue(Profile.objects.filter(user=self.user).exists())
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.first_name, 'Atanas')
        self.assertEqual(self.user.last_name, 'Stankin')
        self.assertEqual(self.user.email, 'astankin@abv.bg')

    def test_if_profile_is_created_when_create_user(self):
        profile = Profile.objects.get(user=self.user)
        self.assertEqual(profile.user, self.user)
        self.assertEqual(str(profile), 'testuser Profile')

    def test_invalid_username(self):
        invalid_username = 'Atanas1'
        with self.assertRaises(ValidationError) as context:
            user_name_validator(invalid_username)
        self.assertEqual('Only letters are allowed', context.exception.message)



