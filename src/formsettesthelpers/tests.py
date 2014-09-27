from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from formsettesthelpers import *
from formsettesthelpers.test_app.forms import UserFormSet, PersonFormSet


class TestModelFormSet(TestCase):
    def test_modelformset(self):
        fh = ModelFormSetHelper(UserFormSet)
        data = fh.generate([
            {'username': 'user1', 'email': 'e@mail.com'},
            {'username': 'user2', 'email': 'e2@mail.com'},
            ], total_forms=2)
        response = self.client.post(reverse('modelformset'), data)
        self.assertEquals(User.objects.count(), 2)


class TestFormSet(TestCase):
    def test_formset(self):
        fh = FormSetHelper(PersonFormSet)
        data = fh.generate([
            {'name': 'Janelle', 'slug': 'j1', 'age': 24},
            {'name': 'Joe', 'slug': 'j2', 'age': 25},
            ], total_forms=2)
        response = self.client.post(reverse('formset'), data)
        self.assertEquals(response.content, 'Is valid')
