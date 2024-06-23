from rest_framework import serializers
from .models import Passanger

class PassangerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passanger
        fields = '__all__'


