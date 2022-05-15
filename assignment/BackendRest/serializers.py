from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from BackendRest.models import Data
# Serializers
class Dataserializer(serializers.ModelSerializer):
    class Meta:
        model=Data
        fields="__all__"