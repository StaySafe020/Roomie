from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    ROLE_CHOICES = [
        ('landlord', 'Landlord'),
        ('tenant', 'Tenant'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
class Landlord(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

class Tenant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

class Property(models.Model):
    address = models.CharField(max_length=255)
    landlord = models.ForeignKey(Landlord, on_delete=models.CASCADE)

class Rental(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()