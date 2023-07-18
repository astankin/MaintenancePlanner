from django.contrib.auth.models import AnonymousUser
from django.contrib.messages import get_messages
from django.contrib.messages.middleware import MessageMiddleware
from django.contrib.sessions.middleware import SessionMiddleware
from django.core.exceptions import ValidationError
from django.test import TestCase, RequestFactory
from django.contrib.auth import get_user_model, authenticate, login
from django.shortcuts import redirect

from MaintenancePlanner.accounts.views import login_user

User = get_user_model()


class LoginUserViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='astankin',
            password='password123',
            first_name='Atanas',
            last_name='Stankin',
            email='astankin@abv.bg',
            role='MANAGER'
        )

    def test_authenticated_user_redirect(self):
        request = self.factory.get('/login/')
        request.user = self.user

        response = login_user(request)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/', fetch_redirect_response=False)

        redirected_response = self.client.get(response.url, follow=True)
        self.assertEqual(redirected_response.status_code, 200)

    def test_valid_credentials_login(self):
        data = {
            'username': 'astankin',
            'password': 'password123'
        }
        request = self.factory.post('/login/', data)
        request.user = AnonymousUser()

        middleware = SessionMiddleware(SessionMiddleware(get_response=lambda r: None))
        middleware.process_request(request)

        response = login_user(request)
        self.assertEqual(response.status_code, 302)

    def test_invalid_credentials_login(self):
        data = {
            'username': 'astankin',
            'password': 'password12345'
        }
        request = self.factory.post('/login/', data)
        request.user = AnonymousUser()
        middleware = SessionMiddleware(SessionMiddleware(get_response=lambda r: None))
        middleware.process_request(request)
        with self.assertRaises(ValidationError) as context:
            login_user(request)
            messages = list(get_messages(request))
        self.assertEqual(len(messages), 1)
    #     self.assertEqual(response.status_code, 200)
    #     # messages = list(get_messages(request))
    #     # self.assertEqual(len(messages), 1)
    #     # self.assertEqual(str(messages[0]),
    #     #                  'Please enter a correct username and password. Note that both fields may be case-sensitive.')
