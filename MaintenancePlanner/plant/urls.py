from django.urls import path

from MaintenancePlanner.plant.views import PlantCreateView, DepartmentCreateView, PlantListView, PlantDeleteView, \
    PlantUpdateView

urlpatterns = [
    path('create/', PlantCreateView.as_view(), name='create-plant'),
    path('department/create/', DepartmentCreateView.as_view(), name='create-department'),
    path('list/', PlantListView.as_view(), name='plants-list'),
    path('delete/<int:pk>/', PlantDeleteView.as_view(), name='delete-plant'),
    path('update/<int:pk>/', PlantUpdateView.as_view(), name='update-plant'),
]