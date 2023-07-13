from django import forms
import django_filters

from MaintenancePlanner.equipment.models import Equipment
from MaintenancePlanner.plant.models import Department, Plant


class EquipmentFilter(django_filters.FilterSet):

    DEPARTMENT_CHOICES = [(department.id, department.name) for department in Department.objects.all()]
    PLANT_CHOICES = [(plant.id, plant.cost_center) for plant in Plant.objects.all()]
    TYPE_CHOICES = [
        ('Machine', 'Machine'),
        ('Measuring tool', 'Measuring tool'),
        ('Mand power tool', 'Hand power tool'),
    ]

    id = django_filters.NumberFilter(
        field_name='id',
        lookup_expr='icontains',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    department = django_filters.ChoiceFilter(
        field_name='department',
        widget=forms.Select(attrs={'class': 'form-control'}),
        choices=DEPARTMENT_CHOICES
    )
    description = django_filters.CharFilter(
        field_name='description',
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    type = django_filters.ChoiceFilter(
        field_name='type',
        widget=forms.Select(attrs={'class': 'form-control'}),
        choices=TYPE_CHOICES  # Replace with the actual choices for 'type' field
    )
    manufacturer = django_filters.CharFilter(
        field_name='manufacturer',
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    plant = django_filters.ChoiceFilter(
        field_name='plant',
        widget=forms.Select(attrs={'class': 'form-control'}),
        choices=PLANT_CHOICES  # Replace with the actual choices for 'plant' field
    )

    class Meta:
        model = Equipment
        fields = ['id', 'description', 'type', 'manufacturer', 'plant', 'department']
