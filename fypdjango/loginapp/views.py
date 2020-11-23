
from django.http import HttpResponse
from django.shortcuts import render
from loginapp.models import usersAuthentication
from rest_framework import viewsets
from .api.serializers import usersAuthenticationSerializer

# Create your views here.2
class userAuthenticationViewSet(viewsets.ModelViewSet):
    queryset = usersAuthentication.objects.all().values()
    #queryset = list(AuthenticationGoogle.objects.all().values())
    # AuthenticationGoogle.objects.filter(email='bsef17a042@pucit.edu.pk')
    
    #print("testing")
    #print(queryset[0].email)
    print(queryset.count())
    serializer_class = usersAuthenticationSerializer

def testingPage(request):
    return HttpResponse("testing page")


