from django.contrib import admin

from .models import Authentication,AuthenticationGoogle
# Register your models here.

admin.site.register(Authentication)

admin.site.register(AuthenticationGoogle)