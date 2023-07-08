from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from MaintenancePlanner.accounts.models import AppUser
from MaintenancePlanner.equipment.forms import EquipmentCreateForm
from MaintenancePlanner.equipment.models import Equipment


# from MaintenancePlanner.profile.models import ProfileModel


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


@login_required()
def create_equipment(request):
    if request.method == 'POST':
        form = EquipmentCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipment-list')
    else:
        form = EquipmentCreateForm()
    context = {
        'form': form
    }
    return render(request, 'create-equipment.html', context)


@login_required()
def edit_equipment(request, pk):
    equipment = Equipment.objects.get(pk=pk)
    if request.method == 'POST':
        form = EquipmentCreateForm(request.POST, instance=equipment)
        if form.is_valid():
            form.save()
            return redirect('equipment-list')
    else:
        form = EquipmentCreateForm(instance=equipment)
    context = {
        'form': form
    }
    return render(request, 'edit-equipment.html', context)


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
