from django.db import models


class Business(models.Model):
    Name = models.CharField(max_length=100)
    TaxID = models.IntegerField(max_length=9)
    Phone = models.IntegerField(max_length=10)
    NAICS = models.IntegerField(max_length=5)
    HasBeenProfitable = models.BooleanField()
    HasBankruptedInLast7Years = models.BooleanField()
    InceptionDate = models.DateTimeField()
    Address = models.OneToOneField('Address',on_delete=models.CASCADE)

class Address(models.Model):
    Address1 = models.TextField()
    Address2 = models.TextField()
    City = models.CharField(max_length=30)
    State = models.CharField(max_length=2)
    Zip = models.IntegerField(max_length=5)

# Create your models here.
