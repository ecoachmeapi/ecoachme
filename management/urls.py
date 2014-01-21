from django.conf.urls.defaults import patterns, include, url
from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from management.models import trainer, workout
from management.views import trainer_detail, trainer_session, workout_detail
from jqchat.views import window, Ajax, BasicAjaxHandler
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from django.core.cache import cache
cache.clear()
urlpatterns = patterns('',
    url(r"^room/(?P<id>\d+)/$", window, name="jqchat_test_window"),
    url(r"^room/(?P<id>\d+)/ajax/$", BasicAjaxHandler, name="jqchat_ajax"),
    url(r'^trainer/(?P<pk>[-_\w]+)/$', trainer_detail.as_view()),
    url(r'^workout/(?P<pk>[-_\w]+)/$', workout_detail.as_view()),
    url(r'^session/(?P<pk>[-_\w]+)/$', trainer_session.as_view()),
    url(r'^featuredtrainers', ListView.as_view(queryset=trainer.objects.all().filter(featured=True),
        template_name="uilist_trainers.html")),
    url(r'^spotworkouts', ListView.as_view(queryset=workout.objects.all().filter(spotlighted=True),
        template_name="uilist_workouts.html")),
    url(r'^allworkouts', ListView.as_view(queryset=workout.objects.all(),
        template_name="allworkouts.html")),
    url(r'^alltrainers', ListView.as_view(queryset=trainer.objects.all(),
            template_name="alltrainers.html")),

)