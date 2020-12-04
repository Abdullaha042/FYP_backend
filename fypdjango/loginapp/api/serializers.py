
from rest_framework import serializers
from loginapp.models import  usersAuthentication,Post

class usersAuthenticationSerializer(serializers.ModelSerializer):
    class Meta:
        model = usersAuthentication
        fields = ('name','username','department','password')


    #def to_internal_value(self, data):
    #    validated = {
    #        'name': data.get('name'),
    #        'username': data.get('username'),
    #        'department': data.get('department'),
    #        'password': int(data.get('password')) + 100,
    #    }
    #    return validated



class PostSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'author', 'description', 'content', 'status')
        model = Post