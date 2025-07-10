from django.urls import path
from . import views

app_name = 'HistoryApp'

urlpatterns = [
    path('', views.HistoryAPIView.as_view(), name='HistoryApp'),
    path('<int:pk>', views.HistoryDetailAPIView.as_view(), name='HistoryApp'),
    path('call-history/', views.CustomerListAPIView.as_view(), name='customer-list'),
    path('shop-detail/<int:pk>/', views.CustomerDetailAPIView.as_view(), name='customer-detail'),
    path('update-customer-detail/', views.UpdateCustomerDetailView.as_view(), name='update-customer-detail'),



 

    path('sale-sessions/', views.SaleSessionListAPIView.as_view(), name='salesession-list'),
    path('create-sale-session/', views.CreateSaleSessionView.as_view(), name='sale-session-create'),
    path('case-sessions-update/<int:pk>/', views.SaleSessionUpdateAPIView.as_view(), name='salesession-update'),
    path('case-sessions-detail/<int:pk>/', views.SaleSessionDetailAPIView.as_view(), name='salesession-detail'),

]