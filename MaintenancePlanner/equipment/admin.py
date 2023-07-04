from django.contrib import admin

from MaintenancePlanner.equipment.models import Equipment, Department


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    pass


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass
