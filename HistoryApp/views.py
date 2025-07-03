from .filters import HistoryFilter
from .models import HistoryModel
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination
from .serializers import HistoryModelSerializer
from django_filters.rest_framework import DjangoFilterBackend


class CustomPagination(PageNumberPagination):
    page_size = 6


    def get_paginated_response(self, data):
        response_data = {
            "count": self.page.paginator.count,
            "next": self.get_next_link(),
            "previous": self.get_previous_link(),
            'totalPages': self.page.paginator.num_pages,
            'currentPage': self.page.number,
            'results': data
        }

        return Response(response_data)

class HistoryAPIView(ListAPIView):
    serializer_class = HistoryModelSerializer
    pagination_class = CustomPagination

    queryset = HistoryModel.objects.filter(user_id=3)
    filter_backends = [DjangoFilterBackend]
    filterset_class = HistoryFilter



class HistoryDetailAPIView(RetrieveAPIView):
    serializer_class = HistoryModelSerializer
    queryset = HistoryModel.objects.all()