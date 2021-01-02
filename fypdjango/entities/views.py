from django.shortcuts import render
from .models import Entity,Attributes
from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import entitySerializer,attributesSerializer

# Create your views here.

class postStaffViewSet(viewsets.ModelViewSet):
    queryset = Entity.objects.all().values()
    serializer_class = entitySerializer

class postAttributesViewSet(viewsets.ModelViewSet):
    queryset = Attributes.objects.all().values()
    serializer_class = attributesSerializer

class staffAttributesViewSet(viewsets.ModelViewSet):
    queryset = Attributes.objects.filter(entity_type="Staff")
    serializer_class = attributesSerializer


class thingAttributesViewSet(viewsets.ModelViewSet):
    queryset = Attributes.objects.filter(entity_type="Thing")
    serializer_class = attributesSerializer


class departmentAttributesViewSet(viewsets.ModelViewSet):
    queryset = Attributes.objects.filter(entity_type="Department")
    serializer_class = attributesSerializer