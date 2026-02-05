from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import Medicines
from .serializers import  MedcicinesSerializer


class Medicineapi(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        
        med = Medicines.objects.all()
        serializer= MedcicinesSerializer(med,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    

    def get (self , request):
        search_by_name=request.query_params.get("search")
        print("done worked")
        if search_by_name:
            med = Medicines.objects.filter(name__icontains=search_by_name)
            print("Worked")
        else:
            med=Medicines.objects.all()
        serializer= MedcicinesSerializer(med,many=True)
        return Response(serializer.data)         
    

    def get(self, request, pk):
        try:
            med = Medicines.objects.get(id=pk)
        except Medicines.DoesNotExist:
            return Response(
                {"error": "Medicine not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = MedcicinesSerializer(med)
        return Response(serializer.data) 

    def post(self, request):
        name = request.data.get("name")
        brand = request.data.get("brand")
        dosage = request.data.get("dosage")

        if Medicines.objects.filter(
            name=name,
            brand=brand,
            dosage=dosage
        ).exists():
            return Response(
                {"error": "Medicine already exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = MedcicinesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Medicine created successfully"},
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
