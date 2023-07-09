from django.urls import path

from MaintenancePlanner.equipment import views
from MaintenancePlanner.equipment.views import CreateEquipment, UpdateEquipment

urlpatterns = [
    path('equipment-list/', views.equipment_list, name='equipment-list'),
    path('<int:pk>/details/', views.view_equipment, name='view-equipment'),
    path('create/', CreateEquipment.as_view(), name='create-equipment'),
    path('<int:pk>/edit/', UpdateEquipment.as_view(), name='edit-equipment'),
    path('<int:pk>/delete/', views.delete_equipment, name='delete-equipment'),
    path('search/', views.search_equipment, name='search-equipment'),
]
