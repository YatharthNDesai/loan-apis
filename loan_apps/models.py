from django.db import models


class LoanApplication(models.Model):
    name = models.CharField(max_length=1,null=True)
    # RequestHeader = models.OneToOneField('RequestHeader',on_delete=models.CASCADE,null=True)
    # Business = models.OneToOneField('Business',on_delete=models.CASCADE,null=True)
    # CFApplicationData = models.OneToOneField('CFApplicationData',on_delete=models.CASCADE,null=True)
    
class RequestHeader(models.Model):
    LoanApplication = models.OneToOneField(LoanApplication,on_delete=models.CASCADE,null=True, related_name='RequestHeader')
    CFRequestId = models.IntegerField()
    RequestDate = models.DateTimeField()
    CFApiUserId = models.CharField(max_length=50, null=True)
    CFApiPassword = models.CharField(max_length=50, null=True)
    IsTestLead = models.BooleanField()


class Business(models.Model):
    LoanApplication = models.OneToOneField(LoanApplication,on_delete=models.CASCADE,null=True, related_name='Business')
    Name = models.CharField(max_length=100)
    TaxID = models.IntegerField(max_length=9)
    Phone = models.IntegerField(max_length=10)
    NAICS = models.IntegerField(max_length=5)
    HasBeenProfitable = models.BooleanField()
    HasBankruptedInLast7Years = models.BooleanField()
    InceptionDate = models.DateTimeField()

class SelfReportedCashFlow(models.Model):
    Business = models.OneToOneField(Business,on_delete=models.CASCADE, null=True, related_name='SelfReportedCashFlow')
    AnnualRevenue = models.DecimalField(max_digits=20,decimal_places=2)
    MonthlyAverageBankBalance = models.DecimalField(max_digits=20,decimal_places=2)
    MonthlyAverageCreditCardVolume = models.DecimalField(max_digits=20,decimal_places=2)

class Owner(models.Model):
    LoanApplication = models.ForeignKey(LoanApplication,on_delete=models.CASCADE,null=True, related_name='Owners')
    Name = models.CharField(max_length=100)
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Email = models.EmailField()
    DateOfBirth= models.DateTimeField()
    HomePhone = models.IntegerField()
    SSN = models.IntegerField()
    PercentageOfOwnership = models.IntegerField()

class Address(models.Model):
    Business = models.OneToOneField(Business,on_delete=models.CASCADE, null=True, related_name='Address')
    Owner = models.OneToOneField(Owner,on_delete=models.CASCADE, null=True, related_name='HomeAddress')
    Address1 = models.TextField()
    Address2 = models.TextField(null=True)
    City = models.CharField(max_length=30)
    State = models.CharField(max_length=2)
    Zip = models.IntegerField(max_length=5)

class CFApplicationData(models.Model):
    LoanApplication = models.OneToOneField(LoanApplication,on_delete=models.CASCADE,null=True, related_name="CFApplicationData")
    RequestedLoanAmount = models.DecimalField(max_digits=20,decimal_places=2)
    StatedCreditHistory = models.IntegerField()
    LegalEntityType = models.CharField(max_length=50)
    FilterID = models.IntegerField()


    # Create your models here.
