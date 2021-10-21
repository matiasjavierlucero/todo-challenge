import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from .models import Task


@pytest.mark.django_db
def test_task_view():
    task = Task.objects.create(
        title="test", description="test description", status=2
    )

    url = reverse("tasks:task-list")
    client = APIClient()

    response = client.get(url)
    print(response)
    assert response.json() == [
        dict(
            id=task.id,
            title='test',
            description='test description',
            status=2,
            created=task.created.isoformat()
        )
    ]


@pytest.mark.django_db
def test_task_status_fail():
    url = reverse("tasks:task-list")
    client = APIClient()

    response = client.post(
        url,
        data=dict(
            title="test",
            description="test description",
            status=3)
    )
    assert response.status_code == 400
