from rest_framework import serializers
from .models import Entity,Attributes,Entity_Description

class entitySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id','entity_name','entity_type','entity_desc_type', 'entity_attributes')
        model = Entity


class attributesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('entity_type', 'field_info')
        model = Attributes



class entityDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name','type', 'attributes')
        model = Entity_Description