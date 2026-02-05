from django.urls import path
from .views import Medicineapi

urlpatterns = [
    path("", Medicineapi.as_view(), name="medicines"),
    path("name/<str:name>/", Medicineapi.as_view(), name="medicine-by-name"),
    path("id/<int:pk>/", Medicineapi.as_view(), name="medicine-by-id")
]