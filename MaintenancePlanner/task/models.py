from django.db import models

from MaintenancePlanner.accounts.models import AppUser
from MaintenancePlanner.equipment.models import Equipment


# Create your models here.
class Task(models.Model):
    technician = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    equipment = models.ForeignKey(
        to=Equipment,
        on_delete=models.CASCADE,
    )
    title = models.CharField(
        max_length=256,
    )
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']
