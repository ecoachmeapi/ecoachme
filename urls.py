from django.conf.urls.defaults import patterns, include, url

from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from site_regions.models import config

# Uncomment the next two lines to enable the admin:
from ecoachme_app.views import indextemplate
from django.contrib import admin
admin.autodiscover()
from django.core.cache import cache
cache.clear()
from tastypie.api import Api;
from signup.api import SignupResource, SchedulingResource;
from specialties.api import SpecialtyResource;
from qualifications.api import QualtificationResource;
from management.api import TrainerResource;
V1_api = Api(api_name='V1');
V1_api.register(SignupResource());
V1_api.register(SchedulingResource());
V1_api.register(SpecialtyResource());
V1_api.register(QualtificationResource());
V1_api.register(TrainerResource());

urlpatterns = patterns('',
    # Uncomment the next line to enable the admin:
    url(r'^jqchat/', include('jqchat.urls')),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^management/', include('management.urls')),
    url(r'^site_regions/', include('site_regions.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^',RedirectView.as_view(url='/static/static/index.html'))
    url(r'^(?P<pk>[-_\w]+)/$', indextemplate.as_view(), name='index'),
    #url(r'^', RedirectView.as_view(url='/' + config.objects.order_by('-odr')[0].id + '/')),
    url(r'^oauth2/', include('provider.oauth2.urls',namespace='oauth2')),
    url(r'^api/', include(V1_api.urls)),

)
