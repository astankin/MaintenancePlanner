from django.contrib.auth.views import  LogoutView
from django.urls import path

from MaintenancePlanner.accounts import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('profile/update/', views.profile_update, name='profile-update')
]
