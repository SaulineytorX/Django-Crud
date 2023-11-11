from rest_framework import serializers
from .models import Project
from tasks.models import Task

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'technology', 'created_at')
        read_only_fields = ('created_at',) # con esto no se puede modificar el created_at
        
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'created', 'datecompleted', 'important', 'user_id')
        read_only_fields = ('created', 'user_id',)