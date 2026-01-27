from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Medicines

class MedcicinesSerializer(serializers.ModelSerializer):
    
    class Meta:
        models=Medicines
        fields = [
           "name",
           "brand",
           "description",
           "price",
           "stock",
           "dosege",
           "required_prescriptions",
           "created_on",
           "updated_on",
    
        ]