from django.test import TestCase
from django.urls import reverse
from .models import Task

class TaskAppTests(TestCase):
    def test_home_page_loads(self):
        response = self.client.get(reverse("task_list"))
        self.assertEqual(response.status_code, 200)

    def test_add_task(self):
        response = self.client.post(reverse("task_list"), {"title": "Django seekhna"})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Task.objects.filter(title="Django seekhna").exists())
