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
from specialties.documents import Specialties
@csrf_exempt
class SpecialtyResource(resources.MongoEngineResource):
    class Meta:
        queryset =  Specialties.objects.all()
        resource_name = 'specialty'
        authorization= Authorization()
        allowed_methods = ('get', 'post', 'put', 'delete')