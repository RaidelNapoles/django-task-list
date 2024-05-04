from django.test import TestCase
from .models import Task
from django.contrib.auth.models import User


class TaskModelTest(TestCase):
    def setUp(self):
        self.test_user = User.objects.create_user(username='admin', password='admin2020')
        self.task = Task.objects.create(
            title='Test Task',
            description='Task created for testing purposes',
            owner=self.test_user
        )
    
    def test_object_name_is_title(self):
        task = Task.objects.get(id=1)
        expected_object_name = f'{task.title}'
        self.assertEqual(str(task), expected_object_name)
