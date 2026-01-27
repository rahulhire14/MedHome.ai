from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models  import  Medicines
from  .seralizers import MedcicinesSerializer

class Medicineapi(APIView):
    permission_classes= [IsAuthenticated]

def post(self , request):
    if Medicines.objects.filter(Medicines=request.Medicines).exists:
        return Response(
        {"error": "Medicines already exists"},
        status=status.HTTP_400_BAD_REQUEST
        )
    serializer=MedcicinesSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(Medicines=request.Medicines)
        return Response(
            {"medicine created"},
              status=status.HTTP_201_CREATED
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)