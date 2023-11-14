from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('tasks/', views.tasks, name='tasks'),
    path('tasks_completed/', views.tasks_completed, name='tasks_completed'),
    path('tasks/create', views.create_task, name='create_task'),
    path('tasks/<int:task_id>/', views.task_detail, name='task_detail'), # Agrega la ruta para editar una tarea
    path('tasks/<int:task_id>/complete', views.complete_task, name='complete_task'), # Agrega la ruta para completar una tarea
    path('tasks/<int:task_id>/delete', views.delete_task, name='delete_task'), # Agrega la ruta para eliminar una tarea
    path('logout/', views.signout, name='logout'),
    path('login/',views.loginuser,name='login'),
    #VIEWS CLIENTS
    path('clients/', views.clients, name='clients'),
    path('clients/view_clients', views.clients_view, name='view_clients'),
    path('clients/create', views.create_clients, name='create_client'),
    path('clients/<int:client_id>/', views.client_detail, name='client_detail'), # Agrega la ruta para editar un cliente
    
    path('clients/<int:client_id>/delete', views.delete_clients, name='delete_client'),
    
    
    #path('clients/<int:client_id>/', views.client_detail, name='client_detail'), # Agrega la ruta para editar un cliente
    #path('clients/<int:client_id>/delete', views.delete_client, name='delete_client'), # Agrega la ruta para eliminar un cliente
    #path('clients/<int:client_id>/edit', views.edit_client, name='edit_client'), # Agrega la ruta para editar un cliente
    
]

