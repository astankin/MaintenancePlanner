from django.urls import path

from MaintenancePlanner.maintenance_plan import views
from MaintenancePlanner.maintenance_plan.views import OperationDetail, ListMp

urlpatterns = [
    path('create-mp/<int:pk>/', views.create_mp, name='create-mp'),
    path('mp-details/<int:pk>/', views.mp_details, name='mp-details'),
    path('create-operation/<int:pk>/', views.create_operation, name='create-operation'),
    path('operation-details/<int:pk>/', OperationDetail.as_view(), name='operation-details'),
    path('operation-delete/<int:pk>/', views.delete_operation, name='delete-operation'),
    path('mp-list/', ListMp.as_view(), name='mp-list'),

]
