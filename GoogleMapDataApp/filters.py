from django_filters import rest_framework as filters
from .models import GoogleMapModel

class GoogleMapFilter(filters.FilterSet):
    servis_type = filters.CharFilter(field_name='search_txt', lookup_expr='icontains')

    class Meta:
        model = GoogleMapModel
        fields = ['servis_type', 'id']
