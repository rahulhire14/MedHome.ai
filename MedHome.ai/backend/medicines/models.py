from django.db import models

class Medicines (models.Model):
   name = models.CharField(max_length=200)
   barnd= models.CharField(max_length=200)
   description=models.TextField(max_length=1000)

   price = models.DecimalField(max_digits=5 , decimal_places=2)
   stock=models.PositiveIntegerField()


   dosege= models.CharField(max_length=10)
   required_prescriptions=models.BooleanField(default=False)

   created_on = models.DateField(auto_now_add=True)
   updated_on = models.DateTimeField(auto_now=True)

def __str__(self):
        return f"{self.name} ({self.dosage})"
