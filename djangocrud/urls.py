from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tasks.urls')),  # Responderá a http://127.0.0.1:8000/
    path('REST/', include('projects.urls')),  # Responderá a http://127.0.0.1:8000/REST/
]
    

