from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .. import views


class TestUrls(SimpleTestCase):

    def run_test(self, name, args, view):
        url = reverse(name, args=args)
        self.assertEquals(resolve(url).func, view)

    def test_home_url_is_resolved(self):
        TestUrls.run_test(self, 'home', [], views.home)

    def test_add_url_is_resolved(self):
        TestUrls.run_test(self, 'add', [], views.add)

    def test_edit_url_is_resolved(self):
        TestUrls.run_test(self, 'edit', ['1'], views.edit)

    def test_updatetaskdata_url_is_resolved(self):
        TestUrls.run_test(self, 'updatetaskdata', ['1'], views.updatetaskdata)

    def test_addworker_url_is_resolved(self):
        TestUrls.run_test(self, 'addworker', [], views.addworker)

    def test_deleteworker_url_is_resolved(self):
        TestUrls.run_test(self, 'deleteworker', ['1'], views.deleteworker)

    def test_update_url_is_resolved(self):
        TestUrls.run_test(self, 'update', ['1'], views.update)

    def test_delete_url_is_resolved(self):
        TestUrls.run_test(self, 'delete', ['1'], views.delete)
