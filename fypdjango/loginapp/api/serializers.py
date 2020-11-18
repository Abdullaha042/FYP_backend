



from rest_framework import serializers
from loginapp.models import Authentication, AuthenticationGoogle
class AuthenticationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Authentication
        fields = ('username', 'email','password')




class AuthenticationGoogleSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthenticationGoogle
        fields = ('email', 'familyName','givenName','googleId','imageUrl','name','password')