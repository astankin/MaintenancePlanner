from django.urls import path

from MaintenancePlanner.task import views
from MaintenancePlanner.task.views import TaskList, UpdateTask, DeleteTask

urlpatterns = [
    path('create-task/<int:pk>/', views.create_task, name='create-task'),
    path('task-list/', TaskList.as_view(), name='task-list'),
    path('update-task/<int:pk>/', UpdateTask.as_view(), name='update-task'),
    path('delete-task/<int:pk>/', DeleteTask.as_view(), name='delete-task'),
]
