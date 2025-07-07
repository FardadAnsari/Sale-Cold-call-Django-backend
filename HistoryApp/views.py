from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from .filters import HistoryFilter
from .models import HistoryModel, CustomerModel, StageModel, SaleSessionModel
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView
from rest_framework.pagination import PageNumberPagination
from .serializers import HistoryModelSerializer, CustomerSerializer, StageSerializer, SaleSessionSerializer
from django_filters.rest_framework import DjangoFilterBackend
from accounts_user.permissions import SelfInfo, Member


class CustomPagination(PageNumberPagination):
    page_size = 4



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
    permission_classes = [Member, SelfInfo]
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return HistoryModel.objects.all()
        return HistoryModel.objects.filter(user_id=user.id)


class CustomerListAPIView(APIView):
    serializer_class = CustomerSerializer
    def get(self, request, *args, **kwargs):
        queryset = CustomerModel.objects.all()
        serializer = CustomerSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class CustomerDetailAPIView(APIView):
    serializer_class = CustomerSerializer

    def get(self, request, pk, *args, **kwargs):
        customer = get_object_or_404(CustomerModel, pk=pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)


class StageListAPIView(APIView):
    serializer_class = StageSerializer
    def get(self, request, *args, **kwargs):
        queryset = StageModel.objects.all()
        serializer = StageSerializer(queryset, many=True)
        return Response(serializer.data)



class SaleSessionListAPIView(ListAPIView):
    queryset = SaleSessionModel.objects.all()
    serializer_class = SaleSessionSerializer


class SaleSessionCreateAPIView(CreateAPIView):
    queryset = SaleSessionModel.objects.all()
    serializer_class = SaleSessionSerializer



class SaleSessionUpdateAPIView(UpdateAPIView):
    queryset = SaleSessionModel.objects.all()
    serializer_class = SaleSessionSerializer
