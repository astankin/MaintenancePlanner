from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView

from MaintenancePlanner.accounts.models import AppUser
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


class CreateEquipment(LoginRequiredMixin, CreateView):
    model = Equipment
    template_name = 'create-equipment.html'
    form_class = EquipmentForm
    success_url = reverse_lazy('equipment-list')


class UpdateEquipment(LoginRequiredMixin, UpdateView):
    model = Equipment
    template_name = 'edit-equipment.html'
    form_class = EquipmentForm
    success_url = reverse_lazy('equipment-list')


@login_required()
def delete_equipment(request, pk):
    equipment = Equipment.objects.get(pk=pk)
    if request.method == 'POST':
        equipment.delete()
        return redirect('equipment-list')


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
