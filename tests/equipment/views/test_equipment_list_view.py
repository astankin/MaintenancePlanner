from django.contrib.auth import get_user_model
from django.test import TestCase, RequestFactory
from django.urls import reverse

from MaintenancePlanner.equipment.models import Equipment
from MaintenancePlanner.plant.models import Plant, Department

AppUser = get_user_model()


class EquipmentListViewTest(TestCase):
    def setUp(self):
        self.plant = Plant.objects.create(
            name='TestPlant',
            country='Bulgaria',
            city='Plovdiv',
            address='Some address',
            cost_center='BG20'
        )
        self.department = Department.objects.create(name='TestDepartment', plant_id=self.plant.id)
        self.user = AppUser.objects.create_user(
            username='astankin',
            password='password123',
            email='astankin@abv.bg',
            role='MANAGER')

    def test_login_user_username_to_be_correct(self):
        credentials = {
            'username': 'astankin',
            'password': 'password123',
        }
        self.client.login(**credentials)

        response = self.client.get(reverse('equipment-list'))
        self.assertEqual('astankin', str(response.context['user']))

    def test_equipment_list_view_when_no_equipment_empty_list(self):
        credentials = {
            'username': 'astankin',
            'password': 'password123',
        }
        self.client.login(**credentials)
        response = self.client.get(reverse('equipment-list'))
        self.assertListEqual([], list(response.context['equipment']))
        self.assertEqual(0, len(list(response.context['equipment'])))

    def test_equipment_list_view_when_expect_list_of_equipment(self):
        credentials = {
            'username': 'astankin',
            'password': 'password123',
        }
        self.client.login(**credentials)
        equipment = Equipment.objects.bulk_create([
            Equipment(
                description='TestEquipment',
                type='Machine',
                plant=self.plant,
                department=self.department,
            ) for i in range(1, 11)
        ])
        response = self.client.get(reverse('equipment-list'))
        self.assertListEqual(equipment, list(response.context['equipment']))
        self.assertEqual(10, len(list(response.context['equipment'])))
