from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView, DeleteView

from MaintenancePlanner.plant.forms import DepartmentCreateForm, PlantCreateForm
from MaintenancePlanner.plant.models import Plant, Department


class PlantCreateView(LoginRequiredMixin, CreateView):
    template_name = 'plant/create-plant.html'
    model = Plant
    form_class = PlantCreateForm
    success_url = '/'


class PlantUpdateView(LoginRequiredMixin, UpdateView):
    pass


class PlantDeleteView(LoginRequiredMixin, DeleteView):
    pass


class DepartmentCreateView(LoginRequiredMixin, CreateView):
    template_name = 'department/create-department.html'
    model = Department
    form_class = DepartmentCreateForm
    success_url = '/'
