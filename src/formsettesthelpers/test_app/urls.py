from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('',
    url(r'^modelformset/$', views.modelformset_view, name='modelformset'),
    url(r'^formset/$', views.formset_view, name='formset'),
    url(r'^prefixedmodelformset/$', views.prefixed_modelformset_view,
        name='prefixed_modelformset'),
    url(r'^prefixedformset/$', views.prefixed_formset_view,
        name='prefixed_formset'),
)
