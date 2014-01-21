__author__ = 'Admin'
# mysite/polls/api.py
from tastypie.resources import ModelResource
from signup.models import Signup as _signup
from tastypie.authentication import BasicAuthentication, ApiKeyAuthentication, MultiAuthentication
from tastypie.authorization import DjangoAuthorization
from signup.ecoachmeauth import ecoachmeauth
from tastypie import fields
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from tastypie.authorization import Authorization

from tastypie_mongoengine import resources
from signup.documents import Signup as SignupData, Scheduling as SchedulingData

@csrf_exempt
class SignupResource(resources.MongoEngineResource):
    class Meta:
        queryset =  SignupData.objects.all()
        resource_name = 'signup'
        authorization= Authorization()
        allowed_methods = ('get', 'post', 'put', 'delete')

class SchedulingResource(resources.MongoEngineResource):
    class Meta:
        queryset =  SchedulingData.objects.all()
        resource_name = 'scheduling'
        authorization= Authorization()
        allowed_methods = ('get', 'post', 'put', 'delete')