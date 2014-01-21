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
from management.documents import management_trainer as Trainer
@csrf_exempt
class TrainerResource(resources.MongoEngineResource):
    class Meta:
        queryset =  Trainer.objects.all()
        resource_name = 'trainer'
        authorization= Authorization()
        allowed_methods = ('get', 'post', 'put', 'delete')