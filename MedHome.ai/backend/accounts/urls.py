from django.urls import path
from .views import registerAPI

urlpatterns = [
    path("register/", registerAPI.as_view(), name="register"),
]