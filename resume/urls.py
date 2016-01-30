from django.conf.urls import url
from . import views
from django.conf.urls.static import static

urlpatterns = [
    #url(r'^$', views.post_list, name='post_list'),
    url(r'^resume/(?P<pk>[0-9]+)/$', views.info_detail, name='info_detail'),
    url(r'^resume/new/$', views.info_new, name='info_new'),
    #url(r'^resume/(?P<pk>[0-9]+)/edit/$', views.info_edit, name='info_edit'),
]