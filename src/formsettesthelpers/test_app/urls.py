from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    url(r'^modelformset/$', views.modelformset, name='modelformset'),
    url(r'^formset/$', views.formset, name='formset'),
)
