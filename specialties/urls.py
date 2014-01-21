from django.conf.urls.defaults import patterns, include, url
from django.views.generic import ListView
from site_regions.models import pagefooter
from site_regions.views import pagefoortDtlVw

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from django.core.cache import cache
cache.clear()

urlpatterns = patterns('',

    #url(r'^specialty/(?P<pk>[-_\w]+)/$', pagefoortDtlVw.as_view(), name='detail'),
    #url(r'^footer', ListView.as_view(queryset=pagefooter.objects.all(),
    #    template_name="uilist_pagefooter.html")),
)
