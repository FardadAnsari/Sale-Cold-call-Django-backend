import django_filters
from .models import HistoryModel, SaleSessionModel
from django.utils import timezone
from django_filters import rest_framework as filters





class HistoryFilter(django_filters.FilterSet):
    date = django_filters.IsoDateTimeFilter(field_name='date',method='filter_date_only')
    sale_session = django_filters.CharFilter(field_name='sale_session__id', lookup_expr='exact')

    class Meta:
        model = HistoryModel
        fields = ['date', 'user_id']

    def filter_date_only(self, queryset, name, value):
        start = timezone.make_aware(
            timezone.datetime.combine(value, timezone.datetime.min.time())
        )
        end = timezone.make_aware(
            timezone.datetime.combine(value, timezone.datetime.max.time())
        )
        return queryset.filter(date__range=(start, end))
    


class SaleSessionFilter(filters.FilterSet):
    created_by = filters.CharFilter(field_name='created_by__username', lookup_expr='icontains')
    last_update =  django_filters.IsoDateTimeFilter(field_name='last_update',method='filter_date_only')

    class Meta:
        model = SaleSessionModel
        fields = ['stage', 'created_by', 'last_update', 'id']


    def filter_date_only(self, queryset, name, value):
        start = timezone.make_aware(
            timezone.datetime.combine(value, timezone.datetime.min.time())
        )
        end = timezone.make_aware(
            timezone.datetime.combine(value, timezone.datetime.max.time())
        )
        return queryset.filter(date__range=(start, end))
    