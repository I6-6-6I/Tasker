from django.test import TestCase, Client
from django.urls import reverse
from ..models import Worker, Task


class TestModels(TestCase):
    def setUp(self):
        self.worker = Worker(name="Stefan")
        self.task = Task(worker=self.worker, title="title", description="desc", status="TODO")

    def test_worker_is_name_not_empty(self):
        self.assertNotEquals(self.worker.name, "")

    def test_worker_is_name_correct(self):
        self.assertEquals(self.worker.name, "Stefan")

    def test_worker_is_correct(self):
        TestModels.test_worker_is_name_not_empty(self)
        TestModels.test_worker_is_name_correct(self)

    def test_task_is_assigned_worker_on_creation(self):
        self.assertEquals(self.task.worker, self.worker)

    def test_task_is_title_not_empty(self):
        self.assertNotEquals(self.task.title, "")

    def test_task_is_description_not_empty(self):
        self.assertNotEquals(self.task.description, "")

    def test_task_is_status_not_empty(self):
        self.assertNotEquals(self.task.status, "")

    def test_task_is_correct(self):
        TestModels.test_task_is_assigned_worker_on_creation(self)
        TestModels.test_task_is_title_not_empty(self)
        TestModels.test_task_is_description_not_empty(self)
        TestModels.test_task_is_status_not_empty(self)
