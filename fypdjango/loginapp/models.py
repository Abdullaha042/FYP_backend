
from django.db import models

# Create your models here.

class usersAuthentication(models.Model):
    name = models.CharField(max_length=120)
    username = models.CharField(max_length=120)
    department = models.CharField(max_length=120)
    password = models.CharField(max_length=120)

    def __str__(self):
        return self.username

    def mytestdepartment(self):
        print("department testing")
        return self.department