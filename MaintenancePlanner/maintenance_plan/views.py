from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import DetailView, ListView

from MaintenancePlanner.equipment.models import Equipment
from MaintenancePlanner.maintenance_plan.forms import CreateMaintenancePlanForm, CreateOperationForm
from MaintenancePlanner.maintenance_plan.models import MaintenancePlanModel, Operation


# Create your views here.
@login_required
def create_mp(request, pk):
    equipment = Equipment.objects.get(pk=pk)
    if request.method == 'POST':
        form = CreateMaintenancePlanForm(request.POST)
        if form.is_valid():
            mp = form.save(commit=False)
            mp.equipment = equipment
            mp.save()
            return redirect('home-page')
    else:
        form = CreateMaintenancePlanForm()
    context = {
        'form': form,
        'equipment': equipment,
    }
    return render(request, 'mp/create-mp.html', context)


@login_required
def mp_details(request, pk):
    mp = MaintenancePlanModel.objects.get(pk=pk)
    operations = Operation.objects.filter(maintenance_plan=mp)
    context = {
        'mp': mp,
        'operations': operations,
    }
    return render(request, 'mp/maintenance-plan.html', context)


@login_required
def create_operation(request, pk):
    mp = MaintenancePlanModel.objects.get(pk=pk)

    if request.method == 'POST':
        form = CreateOperationForm(request.POST)
        if form.is_valid():
            operation = form.save(commit=False)
            operation.maintenance_plan = mp
            operation.save()
            return redirect(reverse('mp-details', kwargs={'pk': pk}))
    else:
        form = CreateOperationForm()

    context = {
        'form': form,
        'mp': mp,
    }
    return render(request, 'operation/create-operation.html', context)


class OperationDetail(LoginRequiredMixin, DetailView):
    model = Operation
    template_name = 'operation/operation-details.html'


@login_required()
def delete_operation(request, pk):
    operation = Operation.objects.get(pk=pk)
    mp = operation.maintenance_plan
    if request.method == 'POST':
        operation.delete()
        return redirect(reverse('mp-details', kwargs={'pk': mp.id}))


class ListMp(LoginRequiredMixin, ListView):
    model = MaintenancePlanModel
    template_name = 'mp/mp-list.html'
