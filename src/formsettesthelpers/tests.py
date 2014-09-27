from django.test import TestCase
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from formsettesthelpers import ModelFormSetHelper
from formsettesthelpers.test_app.forms import UserFormSet


class Test(TestCase):
    def test_modelformset(self):
        fh = ModelFormSetHelper(UserFormSet)
        data = fh.generate([
            {'username': 'user1', 'email': 'e@mail.com'},
            {'username': 'user2', 'email': 'e2@mail.com'},
            ], total_forms=2)
        response = self.client.post(reverse('modelformset'), data)
        self.assertEquals(User.objects.count(), 2)
