from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from .filters import HistoryFilter, SaleSessionFilter
from .models import HistoryModel, CustomerModel, StageModel, SaleSessionModel
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.pagination import PageNumberPagination

from .serializers import HistoryModelSerializer, CustomerSerializer, StageSerializer, CreateSaleSessionSerializer, SaleSessionNameSerializer, CreateHistorySerializer, GetSaleSessionDetailSerializer

from django_filters.rest_framework import DjangoFilterBackend
from accounts_user.permissions import SelfInfo, Member
from GoogleMapDataApp.models import GoogleMapShopsModel
from accounts_user.permissions import Member

class HistoryAPIViewpagination(PageNumberPagination):
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
    
class SaleSessionpagination(PageNumberPagination):
    page_size = 15



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
    permission_classes = [Member, SelfInfo]
    serializer_class = HistoryModelSerializer
    pagination_class = HistoryAPIViewpagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = HistoryFilter

    def get_queryset(self):
        user = self.request.user
        call_param = self.request.query_params.get('call')

        if call_param == 'all':
            return HistoryModel.objects.all()
        else:
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
    
class HistoryAllCallAPIView(ListAPIView):
    permission_classes = [Member]

    serializer_class = HistoryModelSerializer
    pagination_class = HistoryAPIViewpagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = HistoryFilter

    def get_queryset(self):
        return HistoryModel.objects.all()

class CallHistoryViews(APIView):
    permission_classes = [Member]
    serializer_class = CustomerSerializer
    def get(self, request, *args, **kwargs):
        queryset = CustomerModel.objects.all()
        serializer = CustomerSerializer(queryset, many=True)
        return Response(serializer.data)

class UpdateCustomerDetailView(APIView):
    permission_classes=[Member]
    serializer_class = CustomerSerializer

    def put(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomerDetailAPIView(APIView):
    permission_classes = [Member]

    serializer_class = CustomerSerializer

    def get(self, request, pk, *args, **kwargs):
        customer = get_object_or_404(CustomerModel, pk=pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)






class SaleSessionListAPIView(ListAPIView):
    permission_classes = [Member]
    queryset = SaleSessionModel.objects.all()
    serializer_class = SaleSessionNameSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = SaleSessionFilter
    pagination_class = SaleSessionpagination




class GetSaleSessionDetailAPIView(APIView):
    permission_classes = [Member]
    serializer_class = GetSaleSessionDetailSerializer

    def get(self, request, *args, **kwargs):
        sale_session_id = kwargs.get('pk')
        sale_session = get_object_or_404(SaleSessionModel, pk=sale_session_id)
        serializer = self.serializer_class(sale_session)
        return Response(serializer.data)


class SaleSessionDetailAPIView(RetrieveAPIView):
    permission_classes = [Member]
    queryset = SaleSessionModel.objects.all()
    serializer_class = SaleSessionNameSerializer



class CreateSaleSessionView(APIView):
    permission_classes = [Member]
    serializer_class = CreateSaleSessionSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SaleSessionUpdateAPIView(APIView):
    permission_classes = [Member]
    serializer_class = SaleSessionNameSerializer

    def patch(self, request, pk, *args, **kwargs):
        sale_session = get_object_or_404(SaleSessionModel, pk=pk)
        
        serializer = self.serializer_class(sale_session, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class CreateHistoryView(APIView):
    permission_classes = [Member]
    serializer_class = CreateHistorySerializer
    def post(self, request):
        serializer = CreateHistorySerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            return Response({"message": "History created successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)