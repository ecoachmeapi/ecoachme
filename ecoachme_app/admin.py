import django.contrib
from site_regions.models import pagefooter, config
from management.models import trainer, workout
from specialties.models import specialties
from qualifications.models import qualifications
from jqchat.models import *
from jqchat.admin import *

django.contrib.admin.site.register(pagefooter)
django.contrib.admin.site.register(config)

django.contrib.admin.site.register(trainer)

django.contrib.admin.site.register(workout)

django.contrib.admin.site.register(Room, RoomAdmin)
django.contrib.admin.site.register(Message, MessageAdmin)

django.contrib.admin.site.register(specialties)
django.contrib.admin.site.register(qualifications)