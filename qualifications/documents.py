import bson
import mongoengine
import datetime


class InheritableDocument(mongoengine.Document):
    meta = {
        'abstract': True,
        'allow_inheritance': True,
    }


class InheritableEmbeddedDocument(mongoengine.EmbeddedDocument):
    meta = {
        'abstract': True,
        'allow_inheritance': True,
    }


class Qualifications(InheritableDocument):
    name = mongoengine.StringField(max_length=100, required=True, unique=True)
