from rest_framework import serializers

from GoogleMapDataApp.models import GoogleMapModel
from .models import HistoryModel, CustomerModel, StageModel, SaleSessionModel
from GoogleMapDataApp.serializers import GoogleMapSerializer

class HistoryModelSerializer(serializers.ModelSerializer):
    user_id = serializers.CharField(source='user_id.username', read_only=True)
    class Meta:
        model = HistoryModel
        fields = '__all__'



class CustomerSerializer(serializers.ModelSerializer):
    customer_google_business = GoogleMapSerializer(read_only=True)
    shop_id_company = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = CustomerModel
        fields = '__all__'  

    def create(self, validated_data):
        shop_id = validated_data.pop('shop_id_company', None)
        if shop_id:
            try:
                google_business = GoogleMapModel.objects.get(shop_id_company=shop_id)
                validated_data['customer_google_business'] = google_business
            except GoogleMapModel.DoesNotExist:
                raise serializers.ValidationError(
                    {'shop_id_company': f'GoogleMapModel with shop_id_company={shop_id} does not exist.'}
                )
        return super().create(validated_data)


class StageSerializer(serializers.ModelSerializer):
    class Meta:
        model = StageModel
        fields = '__all__'

class SaleSessionSerializer(serializers.ModelSerializer):

    class Meta:
        model = SaleSessionModel
        fields = '__all__'
        read_only_fields = ['created_by',]



