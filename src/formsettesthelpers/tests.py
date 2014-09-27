from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from formsettesthelpers import *
from formsettesthelpers.test_app.forms import UserFormSet, PersonFormSet


class BasicFormsetTestSkeleton(object):
    def setUp(self):
        self.fh = self.helper_class(self.formset_class)

    def test_valid(self):
        data = self.fh.generate(self.two_forms_data, total_forms=2)
        response = self.client.post(reverse(self.view_name), data)
        self.assertEquals(response.content, 'Is valid')

    def test_to_dict(self):
        data = self.fh.generate(self.single_list_data, total_forms=1)
        response = self.client.post(reverse(self.view_name), data)
        self.assertEquals(response.content, 'Is valid')


class TestModelFormSet(BasicFormsetTestSkeleton, TestCase):
    helper_class = ModelFormSetHelper
    formset_class = UserFormSet
    two_forms_data = [
            {'username': 'user1', 'email': 'e@mail.com'},
            {'username': 'user2', 'email': 'e2@mail.com'},
            ]
    single_list_data = [['justin', 'j@mail.org']]
    view_name = 'modelformset'

    def test_valid(self):
        super(TestModelFormSet, self).test_valid()
        self.assertEquals(User.objects.count(), 2)

    def test_to_dict(self):
        super(TestModelFormSet, self).test_to_dict()
        self.assertEquals(User.objects.count(), 1)


class TestFormSet(BasicFormsetTestSkeleton, TestCase):
    helper_class = FormSetHelper
    formset_class = PersonFormSet
    two_forms_data = [
            {'name': 'Janelle', 'slug': 'j1', 'age': 24},
            {'name': 'Joe', 'slug': 'j2', 'age': 25},
            ]
    single_list_data = [['Max', 'max', 42]]
    view_name = 'formset'
