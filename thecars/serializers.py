from rest_framework import serializers
from .models import *

class CarSerializer1(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    type = serializers.StringRelatedField()
    class Meta:
        model = Car
        fields = ['id', 'name', 'year',
                  'type', 'brand', 'photo', 'rating']