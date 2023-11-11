from django.urls import path
from . import views
from rest_framework import routers
from .api import ProjectViewSet, TaskViewSet

router = routers.DefaultRouter()

router.register('api/projects', ProjectViewSet, 'projects')
router.register('api/tasks', TaskViewSet, 'tasks')

urlpatterns = router.urls

