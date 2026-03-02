from rest_framework import serializers
from .models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name', 'timezone']

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

class PwdResetRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()

class PwdResetSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True)