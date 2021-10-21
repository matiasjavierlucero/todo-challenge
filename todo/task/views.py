import re
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from .serializers import TaskSerializer
from .repository import TaskRepository
from .models import Task

class TaskViewSet(ViewSet):
    http_method_names = ['post', 'get', 'retrieve', 'put', 'patch', 'delete']

    def list(self, request, *args, **kwargs):
        task_repository = TaskRepository()
        return Response(TaskSerializer(task_repository.list(), many=True).data)

    def create(self, request, *args, **kwargs):
        task = TaskSerializer(data=request.data)
        task.is_valid(raise_exception=True)
        task.save()
        return Response (task.data)

    def retrieve(self, request, pk=None):
        task_repository = TaskRepository()
        return Response(TaskSerializer(task_repository.detail(id=pk)).data)

    def partial_update(self, request, pk=None):
        task_repository = TaskRepository()
        if request.data.get('status') not in Task.STATUS_CHOICES:
            return Response({"Message" : "Status not in Task.STATUS_CHOICES"})
        return Response(TaskSerializer(task_repository.update(request, id=pk)).data)

    def destroy(self,request , pk=None):
        task_repository = TaskRepository()
        task_repository.destroy(pk)
        return Response({"Message" : "Task deleted successfully"})