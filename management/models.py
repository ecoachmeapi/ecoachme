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
class workout (models.Model):
    def path_and_rename(path):
        def wrapper(instance, filename):
            ext = filename.split('.')[-1];
            filename = '{}.{}'.format(crc32(instance.name+instance.image.name),ext);
            instance.image_filename = filename;
            return os.path.join(path,filename)
        return wrapper
    def path_and_rename_sm(path):
        def wrapper(instance, filename):
            ext = filename.split('.')[-1];
            filename = '{}.{}'.format(crc32(instance.name+instance.imagesm.name),ext);
            instance.imagesm_filename = filename;
            return os.path.join(path,filename)
        return wrapper
    def path_and_rename_icon(path):
        def wrapper(instance, filename):
            ext = filename.split('.')[-1];
            filename = '{}.{}'.format(crc32(instance.name+instance.imageicon.name),ext);
            instance.imageico_filename = filename;
            return os.path.join(path,filename)
        return wrapper
    info = HTMLField(verbose_name="Information")
    odr = models.SmallIntegerField()
    name = models.CharField(max_length=100)
    image = models.ImageField(verbose_name="Workout image", upload_to=path_and_rename(settings.STATICFILES_DIRS[0]+'/img'))
    imagesm = models.ImageField(verbose_name="Workout icon image small",upload_to=path_and_rename_sm(settings.STATICFILES_DIRS[0]+'/img'))
    imageicon = models.ImageField(verbose_name="Workout icon image",upload_to=path_and_rename_icon(settings.STATICFILES_DIRS[0]+'/img'))
    created_at = models.DateField(auto_now_add=True, null=True)
    image_filename = models.CharField(max_length=300, editable=False)
    imagesm_filename = models.CharField(max_length=300, editable=False)
    imageico_filename = models.CharField(max_length=300, editable=False)
    spotlighted = models.BooleanField()
    def trainers(self):
        trainers_self = trainer.objects.filter();
        print("trainers_self.count()");
        print(trainers_self.count());
        return trainers_self;
    def __unicode__(self):
        return self.name;
    class Meta:
        verbose_name = 'Workout'
        verbose_name_plural = 'Workouts'

# Create your models here.
class trainer (models.Model):
    def path_and_rename(path):
        def wrapper(instance, filename):
            ext = filename.split('.')[-1];
            filename = '{}.{}'.format(crc32(instance.name),ext);
            instance.image_filename = filename;
            return os.path.join(path,filename)
        return wrapper
    objects = MongoDBManager()
    info = HTMLField(verbose_name="Bio/Information")
    sess = models.CharField(null=True, blank=True, max_length=500,verbose_name="Tokbox Session ID" )
    token = models.CharField(null=True, blank=True, max_length=500,verbose_name="Tokbox Toke ID" )
    odr = models.SmallIntegerField(null=True, blank=True,)
    name = models.CharField(max_length=100)
    image = models.ImageField(null=True,upload_to=path_and_rename(settings.STATICFILES_DIRS[0]+'/img'), blank=True)
    works =  MongoDBManyToManyField(workout,verbose_name="Workouts from trainer", embed=True)
    featured = models.NullBooleanField(verbose_name="Featured trainer")
    chat_room = models.OneToOneField( Room, blank=True, null=True, help_text='Chat room to be used for this lobby.')
    created_at = models.DateField(auto_now_add=True, null=True)
    image_filename = models.CharField(max_length=300, editable=False)

    def __unicode__(self):
        return self.name;
    class Meta:
        verbose_name = 'Trainer'
        verbose_name_plural = 'Trainers'




@receiver(pre_save, sender=trainer)
def trainer_save(sender, instance, **kwargs):
    if instance.id == None:
        query = Room(name="Trainer's " + instance.name + " chat room")
        query.save()
        instance.chat_room = query