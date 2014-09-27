from django import forms
from django.forms.formsets import formset_factory
from django.forms.models import modelformset_factory
from django.contrib.auth.models import User


UserFormSet = modelformset_factory(
        User, fields=('username', 'email', 'is_staff'))


class PersonForm(forms.Form):
    name = forms.CharField()
    slug = forms.CharField()
    age = forms.IntegerField()

PersonFormSet = formset_factory(PersonForm)
