

class usersAuthenticationSerializer(serializers.ModelSerializer):
    class Meta:
        model = usersAuthentication
        fields = ('name','username','department','password')