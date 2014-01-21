from django.db import models
from tinymce.models import HTMLField
import os
from django.conf import settings
from zlib import *

#from zlib import *
# Create your models here.
class qualifications (models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name;
    class Meta:
        verbose_name = 'Qualification'
        verbose_name_plural = 'Qualifications'

