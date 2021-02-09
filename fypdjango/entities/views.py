from django.shortcuts import render
from .models import Entity,Attributes,Entity_Description
from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import entitySerializer,attributesSerializer,entityDescriptionSerializer

# Create your views here.

class postStaffViewSet(viewsets.ModelViewSet):
    queryset = Entity.objects.all().values()
    serializer_class = entitySerializer






class allStaffMembersViewSet(viewsets.ModelViewSet):
    queryset = Entity.objects.filter(entity_type="User")
    serializer_class = entitySerializer


class allThingsViewSet(viewsets.ModelViewSet):
    queryset = Entity.objects.filter(entity_type="Thing")
    serializer_class = entitySerializer


class allDepartmentsViewSet(viewsets.ModelViewSet):
    queryset = Entity.objects.filter(entity_type="Department")
    serializer_class = entitySerializer


#Entity Configuration
class allEntityConfiguration(viewsets.ModelViewSet):
    queryset = Entity_Description.objects.all().values()
    serializer_class = entityDescriptionSerializer


class staffEntityConfiguration(viewsets.ModelViewSet):
    queryset = Entity_Description.objects.filter(type="User")
    serializer_class = entityDescriptionSerializer

class thingEntityConfiguration(viewsets.ModelViewSet):
    queryset = Entity_Description.objects.filter(type="Thing")
    serializer_class = entityDescriptionSerializer

class departmentEntityConfiguration(viewsets.ModelViewSet):
    queryset = Entity_Description.objects.filter(type="Department")
    serializer_class = entityDescriptionSerializer
