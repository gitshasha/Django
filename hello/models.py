from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.forms import CharField

# Create your models here.


class Destination(models.Model):

    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TimeField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
