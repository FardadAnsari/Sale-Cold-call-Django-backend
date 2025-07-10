from rest_framework import serializers

from GoogleMapDataApp.models import GoogleMapShopsModel
from .models import HistoryModel, CustomerModel, StageModel, SaleSessionModel, SaleUser  
from GoogleMapDataApp.serializers import GoogleMapShopsSerializer

class HistoryModelSerializer(serializers.ModelSerializer):
    user_id = serializers.CharField(source='user_id.username', read_only=True)
    class Meta:
        model = HistoryModel
        fields = '__all__'



class CustomerSerializer(serializers.ModelSerializer):
    customer_google_business = GoogleMapShopsSerializer(read_only=True)
    shop_id_company = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = CustomerModel
        fields = '__all__'  

    def create(self, validated_data):
        shop_id = validated_data.pop('shop_id_company', None)
        if shop_id:
            try:
                google_business = GoogleMapShopsModel.objects.get(shop_id_company=shop_id)
                validated_data['customer_google_business'] = google_business
            except GoogleMapShopsModel.DoesNotExist:
                raise serializers.ValidationError(
                    {'shop_id_company': f'GoogleMapShopsModel with shop_id_company={shop_id} does not exist.'}
                )
        return super().create(validated_data)


class StageSerializer(serializers.ModelSerializer):
    class Meta:
        model = StageModel
        fields = '__all__'





class SaleSessionNameSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(source='created_by.username', read_only=True)
    customer = serializers.CharField(source='customer.customer_name', read_only=True)
    shop= serializers.CharField(source='customer.customer_google_business.shop_name', read_only=True)
    customerDetail= serializers.CharField(source='customer.customer_google_business.shop_id_company', read_only=True)   


    class Meta:
        model = SaleSessionModel
        fields = '__all__'
        read_only_fields = ['created_by',]


class CreateSaleSessionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SaleSessionModel
        fields = '__all__'


class CreateHistorySerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField()
    sale_session_id = serializers.IntegerField()
    call_description = serializers.CharField(source='description', allow_blank=True)
    
    class Meta:
        model = HistoryModel
        fields = ['date', 'user_id','call_time', 'sale_session_id', 'call_description']

    def create(self, validated_data):
        user_id = validated_data.pop('user_id')
        sale_session_id = validated_data.pop('sale_session_id')

        validated_data['user'] = SaleUser.objects.get(id=user_id)
        validated_data['sale_session'] = SaleSessionModel.objects.get(id=sale_session_id)

        return HistoryModel.objects.create(**validated_data)
