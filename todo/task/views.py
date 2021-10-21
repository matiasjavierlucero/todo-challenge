import re
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from .serializers import TaskSerializer
from .repository import TaskRepository
from .models import Task
from rest_framework import filters


class TaskViewSet(ViewSet):
    http_method_names = ['post', 'get', 'retrieve', 'put', 'patch', 'delete']

    def list(self, request, *args, **kwargs):
        queryset = Task.objects.all()
        title = self.request.query_params.get('title')
        date = self.request.query_params.get('date')
        if title:
            queryset = queryset.filter(title=title)
        if date:
            queryset = queryset.filter(created=date)
        return Response(TaskSerializer(queryset, many=True).data)

    def create(self, request, *args, **kwargs):
        task = TaskSerializer(data=request.data)
        task.is_valid(raise_exception=True)
        task.save()
        return Response(task.data)

    def retrieve(self, request, pk=None):
        task_repository = TaskRepository()
        return Response(TaskSerializer(task_repository.detail(id=pk)).data)

    def partial_update(self, request, pk=None):
        task_repository = TaskRepository()
        if request.data.get('status') not in Task.STATUS_CHOICES:
            return Response({"Message": "Status not in Choices"})
        return Response(TaskSerializer(task_repository.update(request, id=pk)).data)

    def destroy(self, request, pk=None):
        task_repository = TaskRepository()
        task_repository.destroy(pk)
        return Response({"Message": "Task deleted successfully"})
