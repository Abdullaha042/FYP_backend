from django.contrib import admin

from .models import usersAuthentication,Post
# Register your models here.

admin.site.register(usersAuthentication)
admin.site.register(Post)