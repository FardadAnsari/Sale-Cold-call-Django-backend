import django_filters
from .models import HistoryModel
from django.utils import timezone

class HistoryFilter(django_filters.FilterSet):
    date = django_filters.IsoDateTimeFilter(field_name='date',method='filter_date_only')

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