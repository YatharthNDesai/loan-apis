from rest_framework import serializers

from loan_apps.models import LoanApplication,Address,Business,SelfReportedCashFlow,RequestHeader,CFApplicationData,Owner


class RequestHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model= RequestHeader
        fields = ['id','CFRequestId','RequestDate','CFApiUserId','CFApiPassword','IsTestLead']


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['Address1','Address2','City','State','Zip']

class SelfReportedCashFlowSerializer(serializers.ModelSerializer):
    class Meta:
        model = SelfReportedCashFlow
        fields = ['AnnualRevenue','MonthlyAverageBankBalance','MonthlyAverageCreditCardVolume']


class BusinessSerializer(serializers.ModelSerializer):
    SelfReportedCashFlow = SelfReportedCashFlowSerializer()
    Address = AddressSerializer()

    class Meta:
        model = Business
        fields = ['Name','TaxID','Phone','NAICS','HasBeenProfitable','HasBankruptedInLast7Years','InceptionDate','SelfReportedCashFlow','Address']
        depth = 2
    
    # def create(self, validated_data):
    #     srcfData = validated_data.pop('SelfReportedCashFlow')
    #     addressData = validated_data.pop('Address')
    #     business = Business.objects.create(**validated_data)
    #     SelfReportedCashFlow.objects.create(Business=business, **srcfData)
    #     Address.objects.create(Business=business,**addressData)
    #     business.save()
    #     return business

class OwnerSerializer(serializers.ModelSerializer):
    HomeAddress = AddressSerializer()
    class Meta:
        model = Owner
        fields = ['Name','FirstName', 'LastName', 'Email' , 'HomeAddress', 'DateOfBirth', 'HomePhone', 'SSN','PercentageOfOwnership']

    # def create(self, validated_data):
    #     HomeAddress = validated_data.pop('HomeAddress')
    #     owner = Owner.objects.create(**validated_data)
    #     Address.objects.create(Owners=owner, **HomeAddress)
    #     return owner

class CFApplicationDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CFApplicationData
        fields = ['RequestedLoanAmount','StatedCreditHistory','LegalEntityType','FilterID']


class LoanApplicationSerializer(serializers.ModelSerializer):
        # SelfReportedCashFlow = SelfReportedCashFlowSerializer()
    RequestHeader = RequestHeaderSerializer()
    Business = BusinessSerializer()
    Owners = OwnerSerializer(many=True)
    CFApplicationData = CFApplicationDataSerializer()
    class Meta:
        model = LoanApplication
        fields = ('id','name', 'RequestHeader','Business', 'Owners','CFApplicationData')
    def create(self, validated_data):
        # srcf = validated_data.pop('SelfReportedCashFlow')
        
       


        reqData = validated_data.pop('RequestHeader')
        owners = validated_data.pop('Owners')
        cfData = validated_data.pop('CFApplicationData')
        business = validated_data.pop('Business')
        srcfData = business.pop('SelfReportedCashFlow')
        addressData = business.pop('Address')
        loanApp = LoanApplication.objects.create(**validated_data)
        Business.objects.create(LoanApplication=loanApp,**business)

    
        # business = Business.objects.create(**validated_data)
        # SelfReportedCashFlow.objects.create(Business=business, **srcfData)
        # Address.objects.create(Business=business,**addressData)
        RequestHeader.objects.create(LoanApplication=loanApp, **reqData)   
        # SelfReportedCashFlow.objects.create(Business=business, **srcfData)
        for owner in owners:
            owner.pop('HomeAddress')
            Owner.objects.create(LoanApplication=loanApp, **owner)
        CFApplicationData.objects.create(LoanApplication=loanApp, **cfData)

        return loanApp 

# class BusinessSerializer(serializers.ModelSerializer):
#     address

