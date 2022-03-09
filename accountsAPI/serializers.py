from rest_framework import serializers
from .models import account, transaction

class accountSerializer(serializers.ModelSerializer):
    account_type_name = serializers.ReadOnlyField(source='account_type.account_type_name')
    class Meta:
        model = account
        fields = '__all__'

class transactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = transaction
        fields = '__all__'
