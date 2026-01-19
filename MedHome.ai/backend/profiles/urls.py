from django.urls import path
from .views import (
    CreateProfileAPIView,
    GetProfileAPIView,
    UpdateProfileAPIView,
)

urlpatterns = [
    path("create/", CreateProfileAPIView.as_view(), name="create-profile"),
    path("me/", GetProfileAPIView.as_view(), name="get-profile"),
    path("update/", UpdateProfileAPIView.as_view(), name="update-profile"),
]
