from rest_framework import serializers
from .models import Process

class processSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','process_name','process_diagram')
        model = Process
