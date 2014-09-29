from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from formsettesthelpers import *
from formsettesthelpers.test_app.forms import UserFormSet, PersonFormSet


class UsageTest(TestCase):
    def test_demonstration(self):
        from django.forms.models import modelformset_factory
        # The following formset is something one could use in a view.
        FormSet = modelformset_factory(User, fields=('username', 'email'))

        # To test such view, we'd need to generate a formset data dict
        # to POST to that view.
        formset_helper = ModelFormSetHelper(FormSet)
        data = formset_helper.generate([
            {'username': 'admin', 'email': 'admin@example.com'},
            {'username': 'user1', 'email': 'userer@example.com'},
            ], total_forms=2)
        # `data` now contains the formset data, something like
        # """{u'form-INITIAL_FORMS': 0, u'form-MAX_NUM_FORMS': 1000,
        #     u'form-1-username': 'user1', u'form-1-email':
        #     'userer@example.com',...}"""
        self.assertEquals(data['form-1-username'], 'user1')

        # The `test_app` application just happens to have such view, so lets
        # use that.
        self.client.post(reverse('modelformset'), data)
        self.assertEquals(User.objects.count(), 2)
        self.assertEquals(User.objects.get(username='admin').email,
                'admin@example.com')
        self.assertEquals(User.objects.get(username='user1').email,
                'userer@example.com')


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

    def test_prefixed(self):
        fh = self.helper_class(self.formset_class, prefix='humans')
        data = fh.generate(
                self.two_forms_data, total_forms=2)
        response = self.client.post(
                reverse('prefixed_%s' % self.view_name), data)
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

    def test_prefixed(self):
        super(TestModelFormSet, self).test_prefixed()
        self.assertEquals(User.objects.count(), 2)


class TestFormSet(BasicFormsetTestSkeleton, TestCase):
    helper_class = FormSetHelper
    formset_class = PersonFormSet
    two_forms_data = [
            {'name': 'Janelle', 'slug': 'j1', 'age': 24},
            {'name': 'Joe', 'slug': 'j2', 'age': 25},
            ]
    single_list_data = [['Max', 'max', 42]]
    view_name = 'formset'
