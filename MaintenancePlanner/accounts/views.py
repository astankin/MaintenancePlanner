from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView

from MaintenancePlanner.accounts.decorators import unauthenticated_user
from MaintenancePlanner.accounts.forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from MaintenancePlanner.accounts.models import AppUser


@unauthenticated_user
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # username = form.cleaned_data.get('username')
            # messages.success(request, f'Account created for {username}! Please Login!')
            return redirect('home-page')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


@unauthenticated_user
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request, user)
            return redirect('home-page')
        else:
            pass
            messages.warning(request,
                             'Please enter a correct username and password. Note that both fields may be case-sensitive.')
    form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'login.html', context)


@login_required
def profile(request):
    return render(request, 'profile/profile.html')


@login_required
def profile_update(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account have been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form,
    }
    return render(request, 'profile/profile-update.html', context)


class ListUsers(LoginRequiredMixin, ListView):
    model = AppUser
    template_name = 'users-list.html'
    context_object_name = 'users'


class DeleteUser(LoginRequiredMixin, DeleteView):
    model = AppUser
    context_object_name = 'users'
    success_url = reverse_lazy('users-list')
