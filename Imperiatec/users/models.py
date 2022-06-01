from cProfile import label
from django.db import models
from django.apps import AppConfig

class User(models.Model):
    eid = models.CharField(max_length=20)
    elogin = models.CharField(max_length=100)
    eemail = models.EmailField()
    epassword = models.CharField(max_length=20)
    class Meta:
        db_table = "user"

class Reservation(models.Model):
    eid = models.CharField(max_length=20)
    edate = models.DateField()
    edebut = models.TimeField()
    eend = models.TimeField()
    ename = models.CharField(max_length=20)
    class Meta:
        db_table = "reservation"
