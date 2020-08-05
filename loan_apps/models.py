from django.db import models


class LoanApplication(models.Model):
    name = models.CharField(max_length=1,null=True)
    RequestHeader = models.OneToOneField('RequestHeader',on_delete=models.CASCADE,null=True)
    Business = models.OneToOneField('Business',on_delete=models.CASCADE,null=True)
    CFApplicationData = models.OneToOneField('CFApplicationData',on_delete=models.CASCADE,null=True)
    
class RequestHeader(models.Model):
    CFRequestID = models.IntegerField()
    RequestDate = models.DateTimeField()
    CFApiUserId = models.CharField(max_length=50)
    CFApiPassword = models.CharField(max_length=50)
    IsTestLead = models.BooleanField()


class Business(models.Model):
    Name = models.CharField(max_length=100)
    SelfReportedCashFlow = models.OneToOneField('SelfReportedCashFlow',on_delete=models.CASCADE,null=True)
    TaxID = models.IntegerField(max_length=9)
    Phone = models.IntegerField(max_length=10)
    NAICS = models.IntegerField(max_length=5)
    HasBeenProfitable = models.BooleanField()
    HasBankruptedInLast7Years = models.BooleanField()
    InceptionDate = models.DateTimeField()
    Address = models.OneToOneField('Address',on_delete=models.CASCADE)

class SelfReportedCashFlow(models.Model):
    AnnualRevenue = models.DecimalField(max_digits=20,decimal_places=2)
    MonthlyAverageBankBalance = models.DecimalField(max_digits=20,decimal_places=2)
    MonthlyAverageCreditCardVolume = models.DecimalField(max_digits=20,decimal_places=2)

class Address(models.Model):
    Address1 = models.TextField()
    Address2 = models.TextField()
    City = models.CharField(max_length=30)
    State = models.CharField(max_length=2)
    Zip = models.IntegerField(max_length=5)

class Owner(models.Model):
    Name = models.CharField(max_length=100)
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Email = models.EmailField(unique=True)
    HomeAddress = models.OneToOneField('Address', on_delete=models.CASCADE)
    DateOfBirth= models.DateTimeField()
    HomePhone = models.IntegerField()
    SSN = models.IntegerField()
    PercentageOfOwnership = models.IntegerField()
    LoanApplication = models.ForeignKey(LoanApplication,on_delete=models.CASCADE,null=True)

class CFApplicationData(models.Model):
    RequestedLoanAmount = models.DecimalField(max_digits=20,decimal_places=2)
    StatedCreditHistory = models.IntegerField()
    LegalEntityType = models.CharField(max_length=50)
    FilterID = models.IntegerField()

    # Create your models here.
