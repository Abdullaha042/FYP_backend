from django.db import models

# Create your models here.

class Entity(models.Model):
    entity_name = models.CharField(max_length=120)
    entity_type = models.CharField(max_length=120)
    entity_attributes = models.JSONField()


class Attributes(models.Model):
    entity_type = models.CharField(max_length=120)
    field_info = models.JSONField()



