"""
Definition of urls for ContactsAssgn.
"""

from django.conf.urls import include, url
from ContactManagerApp import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', ContactsAssgn.views.home, name='home'),
    # url(r'^ContactsAssgn/', include('ContactsAssgn.ContactsAssgn.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^$', views.ContactsListview.as_view(), name='contactlist'),
    url(r'^new/$', views.ContactView.as_view(), name='contact_new'),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.deleteContact, name='contact_delete',),
    url(r'^edit/(?P<pk>[0-9]+)/$', views.EditContact.as_view(), name='contact_edit',),
]
