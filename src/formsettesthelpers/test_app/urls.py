from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    url(r'^modelformset/$', views.modelformset_view, name='modelformset'),
    url(r'^formset/$', views.formset_view, name='formset'),
)
