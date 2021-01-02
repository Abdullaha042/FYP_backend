from rest_framework import serializers
from .models import Entity,Attributes

class entitySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('entity_name','entity_type', 'entity_attributes')
        model = Entity


class attributesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('entity_type', 'field_info')
        model = Attributes
