from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('MaintenancePlanner.common.urls')),
    path('equipment/', include('MaintenancePlanner.equipment.urls')),
    path('user/', include('MaintenancePlanner.accounts.urls')),
    path('plant/', include('MaintenancePlanner.plant.urls')),
    path('maintenance-plan/', include('MaintenancePlanner.maintenance_plan.urls')),
    path('task/', include('MaintenancePlanner.task.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
