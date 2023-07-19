from django.test import TestCase
from django.urls import reverse

from MaintenancePlanner import settings
from MaintenancePlanner.equipment.models import Equipment
from tests.common.test_data import create_plant, create_department, create_user


class CreateEquipmentTest(TestCase):
    def setUp(self):
        self.plant = create_plant()
        self.department = create_department()
        self.user = create_user()

    def test_create_equipment_when_user_is_loggedin_expect_to_create_equipment(self):
        credentials = {
            'username': 'astankin',
            'password': 'password123',
        }
        self.client.login(**credentials)

        form_data = {
            'description': 'TestEquipment',
            'type': 'Machine',
            'currency_code': 'EUR',
            'plant': self.plant,
            'department': self.department,
        }

        response = self.client.post(reverse('create-equipment'), data=form_data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Equipment.objects.count(), 1)
        created_service_report = Equipment.objects.first()
        self.assertEqual(created_service_report.plant, self.plant)

    def test_equipment_creation_if_user_is_unauthenticated_redirect(self):
        response = self.client.post(reverse('create-equipment'))
        self.assertEqual(302, response.status_code)
        expected_redirect_url = f'{settings.LOGIN_URL}?next={reverse("create-equipment")}'
        self.assertEqual(expected_redirect_url, response.headers.get('Location'))
