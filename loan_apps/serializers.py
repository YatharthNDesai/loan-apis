from rest_framework import serializers

from loan_apps.models import LoanApplication

class LoanApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanApplication
        fields = ('id','name', 'RequestHeader', 'Business', 'CFApplicationData')

