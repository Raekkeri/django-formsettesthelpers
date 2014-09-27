from django.views.generic import View
from django.http import HttpResponse

from forms import UserFormSet, PersonFormSet


class ModelFormsetView(View):
    def post(self, request):
        formset = UserFormSet(request.POST)
        if formset.is_valid():
            formset.save()
        return HttpResponse('')


class FormSetView(View):
    def post(self, request):
        formset = PersonFormSet(request.POST)
        if formset.is_valid():
            return HttpResponse('Is valid')
        return HttpResponse('Is not valid')


modelformset = ModelFormsetView.as_view()
formset = FormSetView.as_view()
