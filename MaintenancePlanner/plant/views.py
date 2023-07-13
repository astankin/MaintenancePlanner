from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from MaintenancePlanner.plant.forms import DepartmentCreateForm, PlantCreateForm
from MaintenancePlanner.plant.models import Plant, Department


class PlantCreateView(LoginRequiredMixin, CreateView):
    template_name = 'plant/create-plant.html'
    model = Plant
    form_class = PlantCreateForm
    success_url = reverse_lazy('plants-list')


class PlantUpdateView(LoginRequiredMixin, UpdateView):
    model = Plant
    template_name = 'plant/update-plant.html'
    success_url = reverse_lazy('plants-list')
    form_class = PlantCreateForm


class PlantDeleteView(LoginRequiredMixin, DeleteView):
    model = Plant
    success_url = reverse_lazy('plants-list')
    context_object_name = 'plant'


class PlantListView(LoginRequiredMixin, ListView):
    model = Plant
    template_name = 'plant/plant-list.html'
    context_object_name = 'plants'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        plants = self.get_queryset()
        departments = {plant.id: plant.department_set.all() for plant in plants}
        context['departments'] = departments
        return context


class DepartmentCreateView(LoginRequiredMixin, CreateView):
    template_name = 'department/create-department.html'
    model = Department
    form_class = DepartmentCreateForm
    success_url = '/'
