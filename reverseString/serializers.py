from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import *

class StringtoReverseSerializer(serializers.ModelSerializer):
    	class Meta:
            model = StringtoReverse
            fields = '__all__'