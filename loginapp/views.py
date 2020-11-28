
from django.http import HttpResponse
from django.shortcuts import render
from loginapp.models import usersAuthentication
from rest_framework import viewsets
from .api.serializers import usersAuthenticationSerializer

# Create your views here.2
class userAuthenticationViewSet(viewsets.ModelViewSet):
    queryset = usersAuthentication.objects.all().values()
    #queryset = list(usersAuthentication.objects.all().values())
    #print(usersAuthentication.objects.filter(password='admin'))
    
    #print("testing")
    #print(queryset[0].email)
    print(queryset.count())

    ##creating class and setting vlues in its objects
    obj = usersAuthentication('testN','testU','testD','testP')
    print(obj.mytestdepartment)
    #obj.save()

    serializer_class = usersAuthenticationSerializer

def testingPage(request):
    return HttpResponse("testing page")


