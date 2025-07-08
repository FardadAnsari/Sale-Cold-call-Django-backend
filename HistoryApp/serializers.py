from rest_framework import serializers
from .models import HistoryModel, CustomerModel, StageModel, SaleSessionModel
from GoogleMapDataApp.serializers import GoogleMapSerializer

class HistoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryModel
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    customer_google_business = GoogleMapSerializer(read_only=True)
    class Meta:
        model = CustomerModel
        fields = '__all__'

class StageSerializer(serializers.ModelSerializer):
    class Meta:
        model = StageModel
        fields = '__all__'

class SaleSessionSerializer(serializers.ModelSerializer):

    class Meta:
        model = SaleSessionModel
        fields = '__all__'
        read_only_fields = ['created_by',]



