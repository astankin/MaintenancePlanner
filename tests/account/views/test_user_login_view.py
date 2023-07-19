from django.contrib.auth.models import AnonymousUser
from django.contrib.sessions.middleware import SessionMiddleware
from django.test import TestCase, RequestFactory
from django.contrib.auth import get_user_model
from django.urls import reverse

from MaintenancePlanner.accounts.views import login_user


AppUser = get_user_model()


class LoginUserViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = AppUser.objects.create_user(
            username='astankin',
            password='password123',
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
