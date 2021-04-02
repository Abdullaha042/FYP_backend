from django.db import models

# Create your models here.

class Process(models.Model):
    process_name = models.CharField(max_length=120)
    process_diagram = models.JSONField()
