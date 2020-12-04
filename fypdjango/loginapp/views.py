from django.http import HttpResponse
from django.shortcuts import render
from loginapp.models import usersAuthentication,Post
from rest_framework import viewsets, status
from rest_framework.response import Response

from .api.serializers import usersAuthenticationSerializer, PostSerializer

from django.contrib.auth.models import User

# Create your views here.2
class userAuthenticationViewSet(viewsets.ModelViewSet):
    queryset = usersAuthentication.objects.all().values()
    serializer_class = usersAuthenticationSerializer


class postViewSet(viewsets.ModelViewSet):
    queryset = Post.postobjects.all()#it will convert the database data in a format which the frontend can understand
    serializer_class = PostSerializer