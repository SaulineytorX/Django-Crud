from .models import Project
from tasks.models import Task
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer, TaskSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectSerializer # se importa de serializers.py
    
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = TaskSerializer # se importa de serializers.py
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # Asigna el usuario actual al campo 'user' al crear la tarea