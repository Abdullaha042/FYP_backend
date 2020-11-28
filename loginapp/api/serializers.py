
from rest_framework import serializers
from loginapp.models import  usersAuthentication



class usersAuthenticationSerializer(serializers.ModelSerializer):
    class Meta:
        model = usersAuthentication
        fields = ('name','username','department','password')