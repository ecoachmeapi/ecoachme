from django.db import models
from tinymce.models import HTMLField
import os
from django.conf import settings
from zlib import *

#from zlib import *
# Create your models here.
class pagefooter (models.Model):
    def path_and_rename(path):
        def wrapper(instance, filename):
            ext = filename.split('.')[-1];
            filename = '{}.{}'.format(crc32(instance.title),ext);
            instance.image_filename = filename;
            return os.path.join(path,filename)
        return wrapper
    odr = models.SmallIntegerField()
    title = models.CharField(max_length=100)
    content = HTMLField() #models.CharField(max_length=500)
    video = models.FileField(verbose_name="Video", upload_to=path_and_rename(settings.STATICFILES_DIRS[0]+'/video'))
    video_filename = models.CharField(max_length=300, editable=False)

    def __unicode__(self):
        return self.title;
    class Meta:
        verbose_name = 'Footer'
        verbose_name_plural = 'Footers'


# Create your models here.
class config (models.Model):
    def path_and_rename(path):
        def wrapper(instance, filename):
            ext = filename.split('.')[-1];
            filename = '{}.{}'.format(crc32(instance.title),ext);
            instance.video_filename = filename;
            return os.path.join(path,filename)
        return wrapper
    odr = models.SmallIntegerField()
    title = models.CharField(max_length=100)
    mainpagetext = HTMLField(verbose_name="Main text") #models.CharField(max_length=500)
    mainpagetext_head = HTMLField(verbose_name="Text on page head") #models.CharField(max_length=500)
    main_video = models.FileField(verbose_name="Main Video file",upload_to=path_and_rename(settings.STATICFILES_DIRS[0]+'/video'))
    created_at = models.DateField(auto_now_add=True, null=True)
    video_filename = models.CharField(max_length=300, editable=False)
    def __unicode__(self):
        return self.title;
    class Meta:
        verbose_name = 'Config'
        verbose_name_plural = 'Configs'
