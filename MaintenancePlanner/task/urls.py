from django.urls import path

from MaintenancePlanner.task.views import CreateTask, TaskList, UpdateTask, DeleteTask

urlpatterns = [
    path('create-task/', CreateTask.as_view(), name='create-task'),
    path('task-list/', TaskList.as_view(), name='task-list'),
    path('update-task/<int:pk>/', UpdateTask.as_view(), name='update-task'),
    path('delete-task/<int:pk>/', DeleteTask.as_view(), name='delete-task'),
]
