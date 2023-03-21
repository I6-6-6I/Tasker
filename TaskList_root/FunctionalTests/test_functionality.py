from selenium import webdriver
from ToDoList.models import Worker, Task
from django.contrib.staticfiles.testing import StaticLiveServerTestCase


class TestHomePage(StaticLiveServerTestCase):

    def setUp(self):
        self.worker = Worker(name="Stefan")
        self.worker.save()
        self.task = Task(worker=self.worker, title="title", description="desc", status="TODO")
        self.task.save()
        self.browser = webdriver.Chrome('FunctionalTests/chromedriver.exe')

    def tearDown(self):
        self.browser.close()

    def test_worker_is_displayed(self):
        self.browser.get(self.live_server_url)
        alert = self.browser.find_element('class name', 'WorkerContainer')
        self.assertEquals(
            alert.find_element('class name', 'Worker').text,
            self.worker.name
        )

    def test_task_is_displayed(self):
        self.browser.get(self.live_server_url)
        alert = self.browser.find_element('class name', 'task')
        self.assertEquals(
            alert.find_element('class name', 'TaskTitle').text,
            self.task.title
        )
        self.assertEquals(
            alert.find_element('class name', 'GrayLabel').text,
            self.task.status
        )

    def test_task_update_button_changes_status(self):
        self.browser.get(self.live_server_url)
        self.browser.find_element('class name', 'NextStatus').click()
        self.assertEquals(
            self.browser.find_element('class name', 'YellowLabel').text,
            'InProgress'
        )

    def test_task_edit_button_redirects_to_edit_page(self):
        self.browser.get(self.live_server_url)
        edit_url = self.live_server_url + '/edit/1/'
        self.browser.find_element('class name', 'Edit').click()
        self.assertEquals(
            self.browser.current_url,
            edit_url
        )

    def test_task_save_edited_redirects_to_home_page(self):
        self.browser.get(self.live_server_url)
        home_url = self.live_server_url + '/'
        self.browser.find_element('class name', 'Edit').click()
        self.browser.find_element('class name', 'EditTask').click()
        self.assertEquals(
            self.browser.current_url,
            home_url
        )

