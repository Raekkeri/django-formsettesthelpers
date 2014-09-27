from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from formsettesthelpers import *
from formsettesthelpers.test_app.forms import UserFormSet, PersonFormSet


class BasicFormsetTestSkeleton(object):
    def test_valid(self):
        fh = self.helper_class(self.formset_class)
        data = fh.generate(self.two_forms_data, total_forms=2)
        response = self.client.post(reverse(self.view_name), data)
        self.assertEquals(response.content, 'Is valid')



class TestModelFormSet(BasicFormsetTestSkeleton, TestCase):
    helper_class = ModelFormSetHelper
    formset_class = UserFormSet
    two_forms_data = [
            {'username': 'user1', 'email': 'e@mail.com'},
            {'username': 'user2', 'email': 'e2@mail.com'},
            ]
    view_name = 'modelformset'

    def test_valid(self):
        super(TestModelFormSet, self).test_valid()
        self.assertEquals(User.objects.count(), 2)


class TestFormSet(BasicFormsetTestSkeleton, TestCase):
    helper_class = FormSetHelper
    formset_class = PersonFormSet
    two_forms_data = [
            {'name': 'Janelle', 'slug': 'j1', 'age': 24},
            {'name': 'Joe', 'slug': 'j2', 'age': 25},
            ]
    view_name = 'formset'
