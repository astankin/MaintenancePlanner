from django.contrib.auth.views import  LogoutView
from django.urls import path

from MaintenancePlanner.accounts import views
from MaintenancePlanner.accounts.views import ListUsers, DeleteUser

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/update/', views.profile_update, name='profile-update'),
    path('users-list/', ListUsers.as_view(), name='users-list'),
    path('users-delete/<int:pk>/', DeleteUser.as_view(), name='delete-user'),
]
