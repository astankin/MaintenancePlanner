from django import forms

from MaintenancePlanner.maintenance_plan.models import MaintenancePlanModel, Operation


class CreateMaintenancePlanForm(forms.ModelForm):
    class Meta:
        model = MaintenancePlanModel
        exclude = ('equipment',)


class CreateOperationForm(forms.ModelForm):
    class Meta:
        model = Operation
        exclude = ('maintenance_plan',)

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),

        }



