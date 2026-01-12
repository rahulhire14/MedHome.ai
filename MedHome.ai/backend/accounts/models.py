from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomerUser(AbstractUser):
    email =models.EmailField(unique=True)

    is_customer= models.BooleanField(default=True)
    is_pharmacist = models.BooleanField(default=False)
    is_delivery_partner = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)


    USERNAME_FIELD="email"
    REQUIRED_FIELDS=["username"]

    def __str__(self):
        return self.email