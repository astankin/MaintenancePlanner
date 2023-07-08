from django.contrib import admin

from MaintenancePlanner.maintenance_plan.models import Operation, MaintenancePlanModel
from MaintenancePlanner.task.models import Task


# Register your models here.

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass


@admin.register(MaintenancePlanModel)
class MPAdmin(admin.ModelAdmin):
    pass


@admin.register(Operation)
class MPAdmin(admin.ModelAdmin):
    pass
