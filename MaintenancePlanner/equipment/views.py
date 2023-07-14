from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from MaintenancePlanner.accounts.decorators import allowed_users
from MaintenancePlanner.accounts.mixins import AllowedUsersMixin
from MaintenancePlanner.accounts.models import AppUser
from MaintenancePlanner.equipment.filters import EquipmentFilter
from MaintenancePlanner.equipment.forms import EquipmentForm
from MaintenancePlanner.equipment.models import Equipment


# Create your views here.
@login_required
def equipment_list(request):
    profile = AppUser.objects.first()
    equipment = Equipment.objects.all()
    context = {
        'equipment': equipment,
        'profile': profile,
    }
    return render(request, 'equipment_list.html', context)


@login_required()
def view_equipment(request, pk):
    equipment = Equipment.objects.get(pk=pk)
    return HttpResponseRedirect(reverse('home-page'))


class CreateEquipment(LoginRequiredMixin, AllowedUsersMixin, CreateView):
    allowed_roles = ['MANAGER', 'SUPERVISOR']
    model = Equipment
    template_name = 'create-equipment.html'
    form_class = EquipmentForm
    success_url = reverse_lazy('equipment-list')


class UpdateEquipment(LoginRequiredMixin, AllowedUsersMixin, UpdateView):
    allowed_roles = ['MANAGER', 'SUPERVISOR']
    model = Equipment
    template_name = 'edit-equipment.html'
    form_class = EquipmentForm
    success_url = reverse_lazy('equipment-list')


class DeleteEquipment(LoginRequiredMixin, AllowedUsersMixin, DeleteView):
    allowed_roles = ['MANAGER', 'SUPERVISOR']
    model = Equipment
    success_url = reverse_lazy('equipment-list')


def search_equipment(request):
    if request.method == "POST":
        number = request.POST['number']
        try:
            equipment = Equipment.objects.filter(pk=number)
        except:
            return render(request, 'exception.html')

        context = {
            'number': number,
            'equipment': equipment
        }
        return render(request, 'search-equipment.html', context)
    else:
        return render(request, 'search-equipment.html', {})


def advanced_search_equipment(request):
    equipment = Equipment.objects.all()
    eq_filter = EquipmentFilter(request.GET, queryset=equipment)
    equipment = eq_filter.qs
    context = {
        "eq_filter": eq_filter,
        "equipment": equipment,
    }
    return render(request, 'advanced-search-equipment.html', context)
