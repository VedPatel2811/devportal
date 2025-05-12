from rest_framework import serializers
from django.contrib.auth.models import User
from .models import ApiKey

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

class ApiKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiKey
        fields = ['key', 'created_at']