from django.urls import path
from . import views

app_name = 'HistoryApp'

urlpatterns = [
    path('', views.HistoryAPIView.as_view(), name='HistoryApp'),
    path('<int:pk>', views.HistoryDetailAPIView.as_view(), name='HistoryApp'),
    path('customers/', views.CustomerListAPIView.as_view(), name='customer-list'),
    path('customers/<int:pk>/', views.CustomerDetailAPIView.as_view(), name='customer-detail'),

    path('stages/', views.StageListAPIView.as_view(), name='stage-list'),
    # path('stages/<int:pk>/', views.StageDetailAPIView.as_view(), name='stage-detail'),

    path('sale-sessions/', views.SaleSessionListAPIView.as_view(), name='salesession-list'),

]