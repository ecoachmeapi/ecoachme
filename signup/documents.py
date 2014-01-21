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


class Signup(InheritableDocument):
    user_trainer = mongoengine.StringField(max_length=200)
    name = mongoengine.StringField(max_length=200, required=True, unique=True)
    lastname = mongoengine.StringField(max_length=200, required=True, unique=True)
    password = mongoengine.StringField(max_length=200, required=True, unique=True)
    email = mongoengine.StringField(max_length=200, required=True, unique=True)
    birth = mongoengine.DateTimeField()
    sex = mongoengine.StringField(max_length=10)
    weight = mongoengine.DecimalField()
    weight_goal = mongoengine.DecimalField()
    security_answer_one = mongoengine.StringField(max_length=200)
    security_answer_two = mongoengine.StringField(max_length=200)
    security_answer_three = mongoengine.StringField(max_length=200)
    cellphone = mongoengine.StringField(max_length=200)
    security_answer_three = mongoengine.StringField(max_length=200)


class Scheduling(InheritableDocument):
    className = mongoengine.StringField(max_length=200)
    trainer = mongoengine.StringField(max_length=200, required=True, unique=True)
    date = mongoengine.StringField(max_length=200, required=True, unique=True)
    exerciseAreas = mongoengine.StringField(max_length=200, required=True, unique=True)
    costPerSignup = mongoengine.StringField(max_length=200, required=True, unique=True)
    useLimit = mongoengine.DateTimeField()