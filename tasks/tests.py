from datetime import datetime
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
import time
from .models import Task

# Create your tests here.

class TasksTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username="test1", password="pass")
        testuser1.save()

        test_task = Task.objects.create(
            title="Test Task",
            owner=testuser1,
            description="Tests are happening",
            completed=False,
            due="2022-12-31",
            created_at="2022-01-01"
        )
        test_task.save()

    def test_task_model(self):
        task = Task.objects.get(id=1)
        actual_owner = str(task.owner)
        actual_title = str(task.title)
        actual_description = str(task.description)
        self.assertEqual(actual_owner, "testuser1")
        self.assertEqual(actual_title, "Test Task")
        self.assertEqual(actual_description, "Tests are happening")

    def test_task_list(self):
        url = reverse("task_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        tasks = response.data

        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0]["title"], "Test Task")
    
    def test_get_task_by_id(self):
        url = reverse("task_detail", args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        task = response.data
        self.assertEqual(task["title"], "Test Task")

    def test_create_task(self):
        url = reverse("task_list")
        data = {"owner": 1, "title": "Another Test", "description": "A second test."}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        tasks = Task.objects.all()
        self.assertEqual(len(tasks), 2)
        self.assertEqual(Task.objects.get(id=2).title, "Another Test")

    def test_update_task(self):
        url = reverse("task_detail", args=(1,))
        data = {
            "owner": 1,
            "name": "Updated Task",
            "description": "Now our task is updated.",
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        task = Task.objects.get(id=1)
        self.assertEqual(task.title, data["title"])
        self.assertEqual(task.owner.id, data["owner"])
        self.assertEqual(task.description, data["description"])

    def test_delete_task(self):
        url = reverse("task_detail", args=(1,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        tasks = Task.objects.all()
        self.assertEqual(len(tasks), 0)