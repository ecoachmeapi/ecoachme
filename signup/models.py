from django.db import models
from mongom2m.fields import MongoDBManyToManyField
from django_mongodb_engine.contrib import MongoDBManager
#from django.db.backends.mongoengine.document import DynamicEmbeddedDocument
from tinymce.models import HTMLField
from jqchat.models import Room
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.conf import settings
from zlib import *
import os


# Create your models here.
class Signup (models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
