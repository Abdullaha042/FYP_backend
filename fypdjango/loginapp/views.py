
from django.http import HttpResponse
from django.shortcuts import render
from loginapp.models import Authentication,AuthenticationGoogle
from rest_framework import viewsets
from .api.serializers import AuthenticationGoogleSerializer

# Create your views here.
class AuthenticationGoogleViewSet(viewsets.ModelViewSet):
    queryset = AuthenticationGoogle.objects.all()
    print("testing")
    #print(queryset[0].email)
    print(queryset.count())
    serializer_class = AuthenticationGoogleSerializer





def testingPage(request):
    return HttpResponse("testing page")


