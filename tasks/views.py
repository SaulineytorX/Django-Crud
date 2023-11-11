from django.shortcuts import render, redirect, get_object_or_404 # Importa el método redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm # Crea un formulario de registro de usuario
from django.contrib.auth.models import User # Modelo de usuario de Django
from django.contrib.auth import authenticate, login, logout # Autenticación de usuario de Django
from django.db import IntegrityError # Excepción de integridad de Django
from .forms import TaskForm # Importa el formulario TaskForm
from .models import Task # Importa el modelo Task
from django.utils import timezone # Importa el módulo timezone
from django.contrib.auth.decorators import login_required # Importa el decorador login_required


# Create your views here.
def home(request):
	return render(request,'home.html')

def signup(request):
    if request.method == 'GET':
        return render(request,'signup.html',{
            'form':UserCreationForm()
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                request.POST['username'],
                password=request.POST['password1']
                )
                user.save()
                login(request,user)
                return redirect('tasks')
            except IntegrityError:
                return render(request,'signup.html',{
                    'form':UserCreationForm(),
                    'error':'El usuario ya existe'
                })
        return render(request,'signup.html',{
            'form':UserCreationForm(),
            'error':'Las contraseñas no coinciden'
        })

@login_required       
def tasks(request):
    tasks= Task.objects.filter(user=request.user, datecompleted__isnull=True) # Filtra las tareas por usuario
    return render(request,'tasks/tasks.html',
        {
        'tasks':tasks,
        'title':'Pendientes'
        })

@login_required
def tasks_completed(request):
    tasks= Task.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted') # Filtra las tareas por usuario y ordena por fecha de creación
    return render(request,'tasks/tasks.html',
        {
        'tasks':tasks,
        'title':'Completadas'
        })

@login_required
def create_task(request):  
    if request.method == 'GET':
        return render(request,'tasks/create_task.html',{
            'form':TaskForm
        })
    else:  
        try:
            form = TaskForm(request.POST)
            newtask = form.save(commit=False)
            newtask.user = request.user
            newtask.save()
            return redirect('tasks')
        except ValueError: 
            return render(request,'tasks/create_task.html',{
                'form':TaskForm,
                'error':'Los datos del formulario no son válidos',
            })

@login_required        
def task_detail(request,task_id):
    if request.method == 'GET':
        task = get_object_or_404(Task, pk=task_id, user=request.user) # Obtiene la tarea por id e importa el modelo task y filtra por usuario
        form = TaskForm(instance=task) # Crea una instancia del formulario TaskForm
        return render(request,'tasks/task_detail.html',{
            'task':task,
            'form':form
        })
    else:
        try:
            task = get_object_or_404(Task, pk=task_id, user=request.user) # Obtiene la tarea por id e importa el modelo task y filtra por usuario
            form = TaskForm(request.POST, instance=task) # Crea una instancia del formulario TaskForm
            form.save()
            return redirect('tasks')
        except ValueError: 
            return render(request,'task_detail.html',{
                'task':task,
                'form':form,
                'error':'Los datos del formulario no son válidos',
            })
            
@login_required                        
def complete_task(request,task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user) # Obtiene la tarea por id e importa el modelo task y filtra por usuario
    if request.method == 'POST':
        task.datecompleted = timezone.now()
        task.save()
        return redirect('tasks')

@login_required
def delete_task(request,task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user) # Obtiene la tarea por id e importa el modelo task y filtra por usuario
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')

@login_required
def signout(request):
    logout(request)
    return redirect('home')

def loginuser(request):
    if request.method == 'GET':
        return render(request,'login.html',{
        'form':AuthenticationForm()
    })
    else:
        user = authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user is None: 
            return render(request,'login.html',{
            'form':AuthenticationForm(),
            'error' : "Usuario o contraseña incorrecto"
            })
        else:
            login(request,user)
            return redirect('tasks')