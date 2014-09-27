from django.views.generic import View
from django.http import HttpResponse

from forms import UserFormSet


class ModelFormsetView(View):
    def post(self, request):
        formset = UserFormSet(request.POST)
        if formset.is_valid():
            formset.save()
        return HttpResponse('')


modelformset = ModelFormsetView.as_view()
