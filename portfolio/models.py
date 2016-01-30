from django.db import models
from django.contrib.auth.models import User

class projects(models.Model):
    url = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    user = models.ForeignKey(User, default=1)
    description = models.CharField(max_length=500)
    language = models.CharField(max_length=200)
    display_type = models.CharField(max_length=200)

class language(models.Model):
    name = models.CharField(max_length=200)
    display_type = models.CharField(max_length=200)
    util = models.CharField(max_length=200)
