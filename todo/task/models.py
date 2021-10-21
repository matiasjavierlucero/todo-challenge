from django.db import models
from model_utils import Choices
from datetime import datetime

class Task(models.Model):
    STATUS_CHOICES = Choices(
        (0, 'todo', 'todo'),
        (1, 'inprogress', 'in_progress'),
        (2, 'complete', 'complete'),
    )

    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField()
    status = models.IntegerField(
        default=STATUS_CHOICES.todo, null=False, blank=False, choices=STATUS_CHOICES)
    created = models.DateTimeField(auto_now_add=True)