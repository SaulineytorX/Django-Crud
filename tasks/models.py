from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True,blank=True) # null=True,blank=True permite que el campo sea opcional
    important = models.BooleanField(default=False) # default=False permite que el campo sea opcional y por defecto es False
    user = models.ForeignKey(User,on_delete=models.CASCADE) # on_delete=models.CASCADE permite que al eliminar un usuario se eliminen todas sus tareas
    
    def __str__(self):
        return self.title + ' - by ' + str(self.user.username)