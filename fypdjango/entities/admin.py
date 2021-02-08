from django.contrib import admin
from .models import Entity,Attributes,Entity_Description

# Register your models here.

admin.site.register(Entity)
admin.site.register(Attributes)
admin.site.register(Entity_Description)
