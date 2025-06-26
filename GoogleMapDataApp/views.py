from django.shortcuts import render
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .serializers import GoogleMapSerializer
from .models import GoogleMapModel


class CustomPagination(PageNumberPagination):
    page_size = 10


    def get_paginated_response(self, data):
        response_data = {
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'totalPages': self.page.paginator.num_pages,
            'currentPage': self.page.number,
            'results': data
        }

        return Response(response_data)


class GoogleMapDataAPIView(ListAPIView):
    pagination_class = CustomPagination
    serializer_class = GoogleMapSerializer



    queryset = GoogleMapModel.objects.only(
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
    filter_backends = [DjangoFilterBackend]
    filterset_fields  = ['search_txt']


    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

