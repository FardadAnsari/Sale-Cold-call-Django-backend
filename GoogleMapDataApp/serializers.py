from rest_framework import serializers
from GoogleMapDataApp.models import GoogleMapModel

class GoogleMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoogleMapModel
        fields = (
            'last_update',
            'shop_id_company',
            'shop_url_company',
            'shop_name',
            'latitude',
            'longitude',
            'address',
            'plus_code',
            'postcode',
            'phone',
            'rating',
            'total_reviews',
            'website',
            'search_txt',
            'category',
            'is_open_now',
            'opening_hours',
            'provider_url',
            'providers',
            'services',
        )
