from django.conf import settings
from django.db import models

class UserProfile(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE)
    

    full_name = models.CharField(max_length=100)

    gender = models.CharField(
        max_length=10,
        choices=[
            ("male", "Male"),
            ("female", "Female"),
            ("other", "Other"),
        ]
    ) 

    PhoneNumber = models.CharField(max_length=15)

    created_on=models.DateField(auto_now_add=True)
    updated_on =models.DateField(auto_now_add=True)


    def __str__(self):
     return self