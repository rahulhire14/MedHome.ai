from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import UserProfile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            "full_name",
            "gender",
            "phone",
            "address",
        ]
