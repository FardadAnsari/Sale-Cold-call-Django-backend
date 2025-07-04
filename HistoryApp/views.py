from rest_framework import status
from .filters import HistoryFilter
from .models import HistoryModel
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination
from .serializers import HistoryModelSerializer
from django_filters.rest_framework import DjangoFilterBackend
from accounts_user.permissions import SelfInfo, Member


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
    permission_classes = [Member,SelfInfo]
    serializer_class = HistoryModelSerializer
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = HistoryFilter


    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return HistoryModel.objects.all()
        return HistoryModel.objects.filter(user_id=user.id)


class HistoryDetailAPIView(RetrieveAPIView):
    serializer_class = HistoryModelSerializer
    queryset = HistoryModel.objects.all()