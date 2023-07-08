from django import forms

from MaintenancePlanner.task.models import Task


class CreateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ('complete', 'equipment')
        widgets = {
            'technician': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'created_on': forms.DateInput(format="%d/%m/%Y", attrs={'class': 'form-control', 'type': 'date'}),

        }


class UpdateTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('complete',)

        widgets = {
            'complete': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'type': "checkbox",
                'id': 'flexCheckDefault',
            }),

        }
