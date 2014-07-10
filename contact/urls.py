from django.conf.urls import patterns, url

from contact import views

urlpatterns = patterns('',
	url(r'^$', views.get_contact, name='index'),		
	url(r'^thanks/$', views.thanks, name='thanks'),
)