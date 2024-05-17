from django.contrib.auth.models import User
from rest_framework import serializers

from .models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ["name", "role", "cpf", "cnpj"]
        extra_kwargs = {
            "name": {"required": True},
            "role": {"required": True},
        }


class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer()

    class Meta:
        model = User
        fields = ["username", "email", "password", "profile"]
        extra_kwargs = {"password": {"write_only": True},
                        "email": {"required": True}}

    def create(self, validated_data):
        profile_data = validated_data.pop("profile")
        user = User.objects.create_user(**validated_data)
        UserProfile.objects.create(user=user, **profile_data)
        return user
