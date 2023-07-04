from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView

from MaintenancePlanner.task.forms import CreateTaskForm, UpdateTaskForm
from MaintenancePlanner.task.models import Task


# Create your views here.
class CreateTask(CreateView):
    model = Task
    template_name = 'create-task.html'
    form_class = CreateTaskForm
    success_url = reverse_lazy('task-list')


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


class DeleteTask(DeleteView):
    model = Task
