from rest_framework import serializers

from GoogleMapDataApp.models import GoogleMapShopsModel
from .models import HistoryModel, CustomerModel, StageModel, SaleSessionModel
from GoogleMapDataApp.serializers import GoogleMapShopsSerializer

class HistoryModelSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user_id.username', read_only=True)
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




class GetSaleSessionDetailSerializer(serializers.ModelSerializer):
    sale_session = serializers.SerializerMethodField()
    customer = serializers.SerializerMethodField()
    googlemaps = serializers.SerializerMethodField()
    history = serializers.SerializerMethodField()

    class Meta:
        model = SaleSessionModel
        fields = ['sale_session', 'customer', 'googlemaps', 'history']

    def get_sale_session(self, obj):
        from .serializers import SaleSessionNameSerializer
        return SaleSessionNameSerializer(obj).data

    def get_customer(self, obj):
        return CustomerSerializer(obj.customer).data

    def get_googlemaps(self, obj):
        customer_data = CustomerSerializer(obj.customer).data
        return customer_data.get('customer_google_business', {})

    def get_history(self, obj):
        history_qs = HistoryModel.objects.filter(sale_session_id=obj.id).order_by('-date')
        return HistoryModelSerializer(history_qs, many=True).data