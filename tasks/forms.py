from django import forms
from .models import Task, Clients
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title','description','important']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Ingresa el título'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Ingresa la descripción'}),
            'important': forms.CheckboxInput(attrs={'class':'form-check-input m-auto'})
        }

from django import forms
from .models import Clients

class CreateClientForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = ['names', 'apellidos', 'edad', 'telefono', 'email', 'nota']

    def __init__(self, *args, **kwargs):
        super(CreateClientForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = False  # Hace que el campo de email no sea requerido






