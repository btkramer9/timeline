from django.conf.urls import url

from . import views


app_name = 'events'
urlpatterns = [
	# ex: /events/
    url(r'^$', views.index, name='collections'),
    # ex: /events/5/
    url(r'^(?P<pk>[0-9]+)/$', views.collection_detail, name='collection_detail'),
    # ex: /events/memory/5/
    url(r'^memory/(?P<memory_id>[0-9]+)/$', views.memory_detail, name='detail'),
    # ex: /events/phase/5/
    url(r'^phase/(?P<phase_id>[0-9]+)/$', views.phase_detail, name='phase_detail'),
]