from decimal import Decimal
from django.db.models import Sum
from django.shortcuts import get_object_or_404
from datetime import date, timedelta
from .models import Task


class TaskRepository:
    def list(self):
        return Task.objects.all()

    
    def create(self, title: str, description: str, status: int):
        return Task.objects.create(
            title=title, description=description, status=status
        )

    def detail(self, id):
        return get_object_or_404(Task, pk=id)
    
    def update(self, request, id):
        task = get_object_or_404(Task, pk=id)
        task.status = request.data.get('status')
        task.save()
        return task
  
    def destroy(self, pk=None):
        task = Task.objects.get(id=pk)
        task.delete()