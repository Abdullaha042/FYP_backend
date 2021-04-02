from django.shortcuts import render
from .models import Process
from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import processSerializer

# Create your views here.

class postProcessViewSet(viewsets.ModelViewSet):
    queryset = Process.objects.all()
    serializer_class = processSerializer


