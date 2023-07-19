from django.contrib.auth import get_user_model

from MaintenancePlanner.equipment.models import Equipment
from MaintenancePlanner.plant.models import Plant, Department

AppUser = get_user_model()


def create_user():
    return AppUser.objects.create_user(
        username='astankin',
        password='password123',
        email='astankin@abv.bg',
        role='MANAGER'
    )


def create_plant():
    return Plant.objects.create(
        name='TestPlant',
        country='Bulgaria',
        city='Plovdiv',
        address='Address',
        cost_center='BG20',
    )


def create_department():
    return Department.objects.create(
        name='TestDepartment',
        plant=create_plant()
    )


def create_equipment():
    return Equipment.objects.create(
        description='TestEquipment',
        type='Machine',
        currency_code='EUR',
        plant=create_plant(),
        department=create_department(),
    )
