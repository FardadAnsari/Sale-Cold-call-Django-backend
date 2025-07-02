from django.shortcuts import render
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .serializers import GoogleMapSerializer
from .models import GoogleMapModel
from .filters import GoogleMapFilter



class CustomPagination(PageNumberPagination):
    page_size = 10


    def get_paginated_response(self, data):
        response_data = {
            'totalPages': self.page.paginator.num_pages,
            'currentPage': self.page.number,
            'results': data
        }

        return Response(response_data)


class GoogleMapDataAPIView(ListAPIView):
    pagination_class = CustomPagination
    serializer_class = GoogleMapSerializer

    queryset = GoogleMapModel.objects.all()

    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields  = ['id', 'servis_type']
    filterset_class = GoogleMapFilter
    search_fields = ['shop_name']

