from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView


# Create your views here.
class CreateMaintenancePlan(LoginRequiredMixin, CreateView):
    pass
