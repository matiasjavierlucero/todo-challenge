from datetime import date
from decimal import Decimal

from rest_framework import serializers

from .models import Task
from .repository import TaskRepository


class TaskSerializer(serializers.ModelSerializer):
    status = serializers.ChoiceField(
        choices=[(0, 'todo'), (1, 'in_progress'),(2, 'complete'),]
    )

    class Meta:
        model = Task
        fields = ["id", "title", "description", "status"]


    def create(self, validated_data):
        task_repository = TaskRepository()
        return task_repository.create(
            title=validated_data["title"],
            description=validated_data["description"],
            status=validated_data["status"]
        )

    def detail(self, obj: Task):
        task_repository = TaskRepository()
        return task_repository.detail(obj.id)
