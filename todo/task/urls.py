from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.schemas import get_schema_view
from .views import TaskViewSet

app_name = 'api'
schema_view = get_schema_view(title='Todo Task', urlconf='task.urls')

router = routers.DefaultRouter()

router.register(r'task', TaskViewSet, basename='task')


urlpatterns = [
    url(r'^', include(router.urls)),
]