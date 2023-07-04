from django.urls import path

from MaintenancePlanner.plant.views import PlantCreateView, DepartmentCreateView

urlpatterns = [
    path('create/', PlantCreateView.as_view(), name='create-plant'),
    path('department/create/', DepartmentCreateView.as_view(), name='create-department'),
]