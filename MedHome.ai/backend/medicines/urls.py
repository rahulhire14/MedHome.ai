from django.urls import path
from .views import Medicineapi

urlpatterns = [
    path("", Medicineapi.as_view(), name="medicines"),
]