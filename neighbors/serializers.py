from rest_framework import serializers
from . import models

class NeighborSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Neighbor 
        fields = ['id', 'password', 'username', 'email', 'verified', 'is_active', 'zipcode', 'neighborhood']
    
    def create(self, validated_data):
        neighbor = models.Neighbor.objects.create(
            email = validated_data['email'],
            username = validated_data['username'],
            zipcode = validated_data['zipcode']
        )
        neighbor.set_password(validated_data['password'])
        neighbor.save()
        return neighbor