from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import UserProfile
from .serializers import ProfileSerializer


class CreateProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Check if profile already exists
        if UserProfile.objects.filter(user=request.user).exists():
            return Response(
                {"error": "Profile already exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = ProfileSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(
                {"message": "Profile created successfully"},
                status=status.HTTP_201_CREATED
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
