from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Medicines

class MedcicinesSerializer(serializers.ModelSerializer):
    
  class Meta:

        model=Medicines

        fields = "__all__"