from rest_framework import serializers
from .models import Student


# Create Serializer that convert data to JSON format
class ItemSerializer(serializers.ModelSerializer):
    class Meta :
        model = Student
        fields = '__all__'

