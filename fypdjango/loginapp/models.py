
from django.db import models

# Create your models here.

class Authentication(models.Model):
    username = models.CharField(max_length=120)
    email = models.CharField(max_length=120)
    password = models.CharField(max_length=120)

    def __str__(self):
        return self.username

#####################################

class AuthenticationGoogle(models.Model):
    email = models.CharField(max_length=120)
    givenName = models.CharField(max_length=120)
    familyName = models.CharField(max_length=120)
    googleId = models.CharField(max_length=120)
    imageUrl = models.CharField(max_length=120)
    name = models.CharField(max_length=120)
    password = models.CharField(max_length=120)

    def __str__(self):
        return self.email