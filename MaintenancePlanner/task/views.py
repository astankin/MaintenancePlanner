from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, UpdateView, DeleteView

from MaintenancePlanner.maintenance_plan.models import Operation, MaintenancePlanModel
from MaintenancePlanner.task.forms import CreateTaskForm, UpdateTaskForm
from MaintenancePlanner.task.models import Task


@login_required
def create_task(request, pk):
    operation = Operation.objects.get(pk=pk)
    mp = operation.maintenance_plan
    if request.method == 'POST':
        form = CreateTaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.equipment = operation.maintenance_plan.equipment
            task.save()
            return redirect(reverse('mp-details', kwargs={'pk': mp.id}))
    else:
        form = CreateTaskForm(instance=operation)
    context = {
        'form': form,
        'operation': operation,
    }
    return render(request, 'create-task.html', context)


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'task-list.html'

    ordering = ['equipment']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(technician=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()
        return context


class UpdateTask(LoginRequiredMixin, UpdateView):
    template_name = 'update-task.html'
    model = Task
    form_class = UpdateTaskForm
    success_url = reverse_lazy('task-list')


class DeleteTask(LoginRequiredMixin, DeleteView):
    model = Task
