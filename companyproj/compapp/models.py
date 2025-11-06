from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=100)
    date_joined = models.DateField()
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=8)
    position = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} - {self.position}"