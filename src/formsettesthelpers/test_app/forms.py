from django.forms.models import modelformset_factory
from django.contrib.auth.models import User


UserFormSet = modelformset_factory(
        User, fields=('username', 'email', 'is_staff'))
