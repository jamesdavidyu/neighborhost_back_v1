from rest_framework import serializers
from . import models

class NeighborSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Neighbor 
        fields = '__all__'