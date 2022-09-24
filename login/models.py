from django.db import models

class user(models.Model):
    username = models.CharField(max_length=30, unique=True)
    email = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)