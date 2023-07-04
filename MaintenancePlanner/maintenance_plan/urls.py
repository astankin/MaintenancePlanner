from django.urls import path

from MaintenancePlanner.maintenance_plan.views import CreateMaintenancePlan

urlpatterns = [
    path('create-mp/', CreateMaintenancePlan.as_view(), name='create-mp'),


]