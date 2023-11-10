from django.contrib import admin
from .models import Task # Importa el modelo Task
# Register your models here.

class TaskAdmin(admin.ModelAdmin): # Crea una clase para administrar el modelo Task
    readonly_fields=('created',) # Crea un campo de solo lectura para el campo created

admin.site.register(Task,TaskAdmin) # Registra el modelo Task en el administrador de Django