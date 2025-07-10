from django_filters import rest_framework as filters
from .models import GoogleMapShopsModel

class GoogleMapFilter(filters.FilterSet):
    service_type = filters.CharFilter(field_name='search_txt', lookup_expr='icontains')

    class Meta:
        model = GoogleMapShopsModel
        fields = ['services', 'id', 'shop_name', 'category', 'shop_id_company']
