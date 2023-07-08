from django.urls import path

from MaintenancePlanner.equipment import views

urlpatterns = [
    path('equipment-list/', views.equipment_list, name='equipment-list'),
    path('<int:pk>/details/', views.view_equipment, name='view-equipment'),
    path('create/', views.create_equipment, name='create-equipment'),
    path('<int:pk>/edit/', views.edit_equipment, name='edit-equipment'),
    path('<int:pk>/delete/', views.delete_equipment, name='delete-equipment'),
    path('search/', views.search_equipment, name='search-equipment'),
]
