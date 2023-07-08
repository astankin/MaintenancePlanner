from django.db import models

from MaintenancePlanner.accounts.models import AppUser
from MaintenancePlanner.equipment.models import Equipment


# Create your models here.


class MaintenancePlanModel(models.Model):
    name = models.CharField(
        max_length=30,
        unique=True,
    )

    def __str__(self):
        return self.name

    equipment = models.OneToOneField(
        to=Equipment,
        on_delete=models.CASCADE,
    )


class Operation(models.Model):
    title = models.CharField(
        max_length=30,
    )
    description = models.TextField()
    maintenance_plan = models.ForeignKey(
        to=MaintenancePlanModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title
