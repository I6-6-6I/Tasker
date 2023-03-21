from django.test import TestCase, Client
from django.urls import reverse
from ..models import Worker, Task
import json

STATUS_CODE_OK = 200
STATUS_CODE_FOUND = 302


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
        self.add_url = reverse('add')
        self.edit_url = reverse('edit', args=['1'])
        self.updatetaskdata_url = reverse('updatetaskdata', args=['1'])
        self.addworker_url = reverse('addworker')
        self.deleteworker_url = reverse('deleteworker', args=['1'])
        self.update_url = reverse('update', args=['1'])
        self.delete_url = reverse('delete', args=['1'])
        self.worker = Worker(name="Stefan")
        self.worker.save()
        self.task = Task(title="task", worker=self.worker, description="desc", status='TODO')
        self.task.save()

    def test_home_get(self):
        response = self.client.get(self.home_url)
        self.assertEquals(response.status_code, STATUS_CODE_OK)
        self.assertTemplateUsed(response, 'home.html')

    def test_add_post(self):
        response = self.client.post(self.add_url, {
            'worker_id': self.worker.id,
            'title': 'task',
            'description': 'desc'
        })
        self.assertEquals(response.status_code, STATUS_CODE_FOUND)
        self.assertEquals(self.task.title, 'task')

    def test_edit_get(self):
        response = self.client.get(self.edit_url)
        self.assertEquals(response.status_code, STATUS_CODE_OK)
        self.assertTemplateUsed(response, 'edit.html')

    def test_updatetaskdata_post(self):
        response = self.client.post(self.updatetaskdata_url, {
            'workers': self.worker.id,
            'title': 'task',
            'description': 'desc'
        })

        self.assertEquals(response.status_code, STATUS_CODE_FOUND)
        self.assertEquals(self.task.title, 'task')

    def test_addworker_post(self):
        response = self.client.post(self.addworker_url, {
            'workername': 'Stefan'
        })

        self.assertEquals(response.status_code, STATUS_CODE_FOUND)
        self.assertEquals(self.worker.name, 'Stefan')

    def test_delete_worker_get(self):
        response = self.client.get(self.deleteworker_url)

        self.assertEquals(response.status_code, STATUS_CODE_FOUND)
        self.assertRedirects(response, '/')

    def test_update_get(self):
        response = self.client.get(self.update_url)

        self.assertEquals(response.status_code, STATUS_CODE_FOUND)
        self.assertRedirects(response, '/')

    def test_delete_get(self):
        response = self.client.get(self.delete_url)

        self.assertEquals(response.status_code, STATUS_CODE_FOUND)
        self.assertRedirects(response, '/')
