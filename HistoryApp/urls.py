from django.urls import path
from . import views

app_name = 'HistoryApp'

urlpatterns = [
    path('', views.HistoryAPIView.as_view(), name='HistoryApp'),
    path('<int:pk>', views.HistoryDetailAPIView.as_view(), name='HistoryApp'),
    path('call-history/', views.CustomerListAPIView.as_view(), name='customer-list'),
    path('shop-detail/<int:pk>/', views.CustomerDetailAPIView.as_view(), name='customer-detail'),
    path('update-customer-detail/', views.UpdateCustomerDetailView.as_view(), name='update-customer-detail'),
    path('create-history/', views.CreateHistoryView.as_view(), name='create_history'),



 

    path('sale-sessions/', views.SaleSessionListAPIView.as_view(), name='salesession-list'),
    path('create-sale-session/', views.CreateSaleSessionView.as_view(), name='sale-session-create'),
    path('sale-sessions-update/<int:pk>/', views.SaleSessionUpdateAPIView.as_view(), name='salesession-update'),
    path('sale-sessions-detail/<int:pk>/', views.SaleSessionDetailAPIView.as_view(), name='salesession-detail'),
    path('get-sale-session/<int:pk>/', views.GetSaleSessionDetailAPIView.as_view(), name='sale-session-detail'),

]