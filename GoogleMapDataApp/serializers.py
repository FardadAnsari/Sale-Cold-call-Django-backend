from rest_framework import serializers
from GoogleMapDataApp.models import GoogleMapShopsModel


class GoogleMapShopsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoogleMapShopsModel
        fields = (
            'id',
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
