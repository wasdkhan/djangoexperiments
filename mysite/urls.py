from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^contact/', include('contact.urls', namespace = "contact")),
    url(r'^contact_form/', include('contact_form.urls', namespace = "contact_form")),
    url(r'^admin/', include(admin.site.urls)),
)